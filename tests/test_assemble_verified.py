import sys
import json
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from assemble_verified import assemble, main


class AssemblyTests(unittest.TestCase):
    def setUp(self):
        self.manifest = [dict(id='ui-0123456789ab', name='Old', url='https://example.com/old', source_file='site_items.json')]
        self.sources = {'site_items.json': [dict(name='Old', url='https://example.com/old/', platform='灵感平台', kind='作品', description='Old description')]}
        self.audit = dict(date='2026-11-03', items=[dict(url='https://example.com/old', result='pass', action='Play', observed='Frames changed', replacement_url='https://cdn.example.com/demo.mp4', suggested_name='New', suggested_description='Observed demo', notes='Only a clip')])

    def test_repaired_video_keeps_original_identity_and_observations(self):
        result = assemble(self.manifest, self.sources, self.audit)
        item = result['items'][0]
        self.assertEqual(item['stable_id'], 'ui-0123456789ab')
        self.assertEqual(item['url'], 'https://cdn.example.com/demo.mp4')
        self.assertEqual((item['name'], item['description']), ('New', 'Observed demo'))
        self.assertEqual((item['kind'], item['platform']), ('视频', '独立站'))
        self.assertEqual(item['verification_observed'], 'Frames changed')
        self.assertEqual(item['audit']['original_url'], 'https://example.com/old')
        self.assertTrue(item['playback_verified'])
        self.assertTrue(result['report']['release_ready'])

    def test_explicit_empty_access_note_clears_stale_candidate_warning(self):
        self.sources['site_items.json'][0]['access_notes'] = 'Needs browser verification'
        self.audit['items'][0]['access_notes'] = ''
        result = assemble(self.manifest, self.sources, self.audit)
        self.assertEqual(result['items'][0]['access_notes'], '')

    def test_verified_video_replaces_candidates_unplayed_status(self):
        source = dict(name='Video', url='https://cdn.example.com/clip.mp4',
                      kind='视频', playback_verified=False,
                      browser_verified=False, visual_verified=False,
                      review_status='candidate', verification='HEAD only; not played')
        review = dict(url=source['url'], result='pass',
                      action='Play clip and compare two frames', observed='Menu expands')
        result = assemble([], {}, [], [source], [[review]], '2026-11-03')
        item = result['items'][0]
        self.assertTrue(item['playback_verified'])
        self.assertTrue(item['browser_verified'])
        self.assertTrue(item['visual_verified'])
        self.assertEqual(item['review_status'], 'verified')
        self.assertEqual(item['verification'], '本轮实际播放片段核查')
        self.assertFalse(source['playback_verified'])

    def test_explicit_unverified_playback_overrides_video_pass(self):
        source = dict(name='Video poster', url='https://cdn.example.com/clip.mp4',
                      kind='视频', playback_verified=True)
        review = dict(url=source['url'], result='pass', playback_verified=False,
                      action='Inspect poster', observed='Static interface visible')
        result = assemble([], {}, [], [source], [[review]], '2026-11-03')
        item = result['items'][0]
        self.assertFalse(item['playback_verified'])
        self.assertTrue(item['visual_verified'])
        self.assertEqual(item['verification'], '本轮实际画面核查（未验证播放）')

    def test_static_webpage_pass_does_not_claim_video_playback(self):
        for stale_playback in (False, True):
            with self.subTest(stale_playback=stale_playback):
                source = dict(name='Static UI', url='https://example.com/interface',
                              kind='在线演示', playback_verified=stale_playback)
                review = dict(url=source['url'], result='pass',
                              action='Inspect page', observed='Static dashboard visible')
                result = assemble([], {}, [], [source], [[review]], '2026-11-03')
                item = result['items'][0]
                self.assertFalse(item['playback_verified'])
                self.assertTrue(item['visual_verified'])
                self.assertEqual(item['verification'], '本轮实际画面与关键操作核查')

    def test_conflicting_audits_and_baseline_identity_collisions_are_errors(self):
        conflicting = dict(self.audit['items'][0], result='fail')
        with self.assertRaisesRegex(ValueError, 'Conflicting audit'):
            assemble(self.manifest, self.sources, [self.audit['items'][0], conflicting], audit_date='2026-11-03')
        manifest = self.manifest + [dict(self.manifest[0], url='https://example.com/other', id='ui-abcdef012345')]
        sources = {'site_items.json': self.sources['site_items.json'] + [dict(self.sources['site_items.json'][0], url='https://example.com/other')]}
        reviews = self.audit['items'] + [dict(self.audit['items'][0], url='https://example.com/other')]
        with self.assertRaisesRegex(ValueError, 'Baseline final URL collision'):
            assemble(manifest, sources, reviews, audit_date='2026-11-03')

    def test_orphan_audit_and_missing_source_are_errors(self):
        with self.assertRaisesRegex(ValueError, 'Unknown baseline audit URL'):
            assemble(self.manifest, self.sources, [dict(self.audit['items'][0], url='https://unknown.example')])
        with self.assertRaisesRegex(ValueError, 'Missing baseline source'):
            assemble(self.manifest, {'site_items.json': []}, self.audit)

    def test_only_complete_pass_records_can_be_admitted(self):
        cases = [({'result': 'fail'}, 'audit_fail', True),
                 ({'result': 'blocked'}, 'audit_blocked', True),
                 ({'result': 'pending'}, 'audit_pending', False),
                 ({'action': '  '}, 'incomplete_pass', False),
                 ({'observed': ''}, 'incomplete_pass', False),
                 ({'quality_recommendation': 'remove'}, 'quality_remove', True)]
        for patch, reason, ready in cases:
            with self.subTest(patch=patch):
                review = dict(self.audit['items'][0], **patch)
                result = assemble(self.manifest, self.sources, dict(date='2026-11-03', items=[review]))
                self.assertEqual(result['items'], [])
                self.assertEqual(result['report']['excluded'][0]['reason'], reason)
                self.assertEqual(result['report']['release_ready'], ready)
        result = assemble(self.manifest, self.sources, [])
        self.assertEqual(result['report']['excluded'][0]['reason'], 'missing_audit')
        self.assertFalse(result['report']['release_ready'])

    def test_candidates_need_their_own_pass_and_duplicate_final_url_keeps_baseline(self):
        candidates = [dict(name='Duplicate', url='https://new.example/one', kind='作品'),
                      dict(name='Unique', url='https://new.example/two/', kind='作品'),
                      dict(name='Pending', url='https://new.example/three', kind='作品')]
        reviews = [dict(url='https://new.example/one', result='pass', action='Play', observed='Motion', replacement_url='https://cdn.example.com/demo.mp4?utm_source=test'),
                   dict(url='https://new.example/two', result='pass', action='Click', observed='Changed')]
        result = assemble(self.manifest, self.sources, self.audit, candidates, [reviews], '2026-11-03')
        self.assertEqual([i['name'] for i in result['items']], ['New', 'Unique'])
        self.assertEqual(len(result['sources']['candidate_verified_items.json']), 1)
        self.assertEqual([i['reason'] for i in result['report']['excluded']], ['duplicate_final_url', 'missing_audit'])
        self.assertTrue(result['report']['release_ready'])

    def test_cli_stages_reproducibly_and_never_overwrites_source(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for name, value in [('manifest.json', self.manifest), ('audit.json', self.audit), ('site_items.json', self.sources['site_items.json'])]:
                (root / name).write_text(json.dumps(value), encoding='utf-8')
            before = (root / 'site_items.json').read_bytes()
            argv = ['--source-root', str(root), '--manifest', str(root / 'manifest.json'), '--baseline-audit', str(root / 'audit.json'), '--out-dir', str(root / 'staged')]
            self.assertEqual(main(argv), 0)
            output = (root / 'staged/assembled_items.json').read_bytes()
            self.assertEqual(main(argv), 0)
            self.assertEqual((root / 'staged/assembled_items.json').read_bytes(), output)
            self.assertEqual((root / 'site_items.json').read_bytes(), before)
            self.assertEqual(main(argv[:-1] + [str(root)]), 2)
            self.assertEqual((root / 'site_items.json').read_bytes(), before)
            pending = dict(self.audit, items=[dict(self.audit['items'][0], result='pending')])
            (root / 'audit.json').write_text(json.dumps(pending), encoding='utf-8')
            self.assertEqual(main(argv), 2)
            self.assertFalse(json.loads((root / 'staged/assembly-report.json').read_text(encoding='utf-8'))['release_ready'])

    def test_pass_without_date_is_reported_and_not_promoted(self):
        result = assemble(self.manifest, self.sources, self.audit['items'])
        self.assertFalse(result['report']['release_ready'])
        self.assertIn('checked_at', result['report']['errors'][0]['message'])

    def test_candidate_pending_is_allowed_but_baseline_pending_blocks_release(self):
        source = dict(name='Later', url='https://later.example')
        pending = dict(url=source['url'], result='pending')
        result = assemble(self.manifest, self.sources, self.audit, [source], [[pending]], '2026-11-03')
        self.assertTrue(result['report']['release_ready'])
        self.assertEqual(result['report']['excluded'][0]['reason'], 'audit_pending')

    def test_invalid_stable_id_and_old_audit_date_cannot_be_released(self):
        with self.assertRaisesRegex(ValueError, 'Invalid baseline stable_id'):
            assemble([dict(self.manifest[0], id='ui-invalid')], self.sources, self.audit)
        old = dict(self.audit, items=[dict(self.audit['items'][0], checked_at='2026-11-02')])
        self.sources['site_items.json'][0]['checked_at'] = '2026-11-03'
        result = assemble(self.manifest, self.sources, old)
        self.assertFalse(result['report']['release_ready'])
        self.assertEqual(result['items'], [])
        self.assertIn('2026-11-03', result['report']['errors'][0]['message'])


if __name__ == '__main__':
    unittest.main()
