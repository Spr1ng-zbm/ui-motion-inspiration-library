const test = require('node:test');
const assert = require('node:assert/strict');
const {filterItems, safeUrl} = require('../web/catalog.js');
const items = [
 {id:'a',name:'React 流体背景',description:'暗色粒子',tags:['WebGL'],category:'粒子与背景',platform:'GitHub',kind:'组件库',featured:true,repo_url:'https://github.com/a/a'},
 {id:'b',name:'UI 作品集',description:'清晰排版',tags:['设计'],category:'完整界面',platform:'B站',kind:'视频',featured:false},
];
test('search combines Chinese and case-insensitive tokens',()=>assert.deepEqual(filterItems(items,{query:'react 背景'}).map(x=>x.id),['a']));
test('multiple filters use intersection',()=>assert.equal(filterItems(items,{query:'UI',platform:'GitHub'}).length,0));
test('favorites and source-only filters work',()=>{
 assert.deepEqual(filterItems(items,{favoritesOnly:true,favorites:new Set(['b'])}).map(x=>x.id),['b']);
 assert.equal(filterItems(items,{sourceOnly:true}).length,1);
});
test('unknown queries give an empty list',()=>assert.equal(filterItems(items,{query:'does-not-exist'}).length,0));
test('URL handling blocks scripts and credentials',()=>{
 assert.equal(safeUrl('javascript:alert(1)'), '');
 assert.equal(safeUrl('https://u:p@example.com'), '');
 assert.equal(safeUrl('https://example.com'), 'https://example.com/');
});
