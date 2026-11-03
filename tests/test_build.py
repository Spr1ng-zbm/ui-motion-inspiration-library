import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import build


class BuildTests(unittest.TestCase):
    def test_canonical_url_keeps_identity_not_tracking(self):
        self.assertEqual(build.canonical_url('https://www.youtube.com/watch?v=ABC_12&utm_source=x&t=8'), 'https://www.youtube.com/watch?v=ABC_12')
        self.assertEqual(build.canonical_url('https://example.com/test/?utm_source=x'), 'https://example.com/test')

    def test_rejects_unsafe_or_missing_urls(self):
        for value in ['javascript:alert(1)', 'file:///c:/secret', '//example.com', 'https://u:p@example.com']:
            with self.assertRaises(ValueError):
                build.canonical_url(value)

    def test_duplicate_sources_merge_without_losing_evidence(self):
        base = dict(name='Example', url='https://example.com/', category='完整界面', platform='独立站', kind='作品', tags=['UI'], description='参考界面', evidence_url='https://example.com', verification='页面信息')
        duplicate = dict(base, url='https://example.com?utm_source=test', tags=['动效'], repo_url='https://github.com/a/b')
        items = build.merge_items([base, duplicate])
        self.assertEqual(len(items), 1)
        self.assertEqual(set(items[0]['tags']), {'UI', '动效'})
        self.assertEqual(items[0]['repo_url'], duplicate['repo_url'])

    def test_script_serialization_cannot_close_script(self):
        out = build.safe_json([{'name': '</script><script>alert(1)</script>'}])
        self.assertNotIn('</script>', out)
        self.assertIn('\\u003c', out)

    def test_duplicate_cannot_inject_unsafe_repository_url(self):
        a = dict(name='A',url='https://example.com',description='A')
        with self.assertRaises(ValueError):
            build.merge_items([a,dict(a,repo_url='javascript:alert(1)')])

    def test_ids_stay_stable_when_order_changes(self):
        a = dict(name='A', url='https://a.com', description='A')
        b = dict(name='B', url='https://b.com', description='B')
        first = {v['url']:v['id'] for v in build.merge_items([a,b])}
        second = {v['url']:v['id'] for v in build.merge_items([b,a])}
        self.assertEqual(first, second)


if __name__ == '__main__':
    unittest.main()
