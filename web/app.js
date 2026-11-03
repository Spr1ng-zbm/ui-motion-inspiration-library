(()=>{
  'use strict';
  const data=JSON.parse(document.getElementById('library-data').textContent);
  const items=data.items, $=id=>document.getElementById(id);
  const state={query:'',category:'',platform:'',kind:'',view:'all',limit:30,previews:true};
  let favorites=new Set(), storageAvailable=true, toastTimer;
  try{ const saved=JSON.parse(localStorage.getItem('motion-index-favorites')||'[]'); if(Array.isArray(saved)) favorites=new Set(saved.filter(x=>typeof x==='string')); }
  catch{storageAvailable=false;}
  const el=(tag,className,text)=>{const n=document.createElement(tag);if(className)n.className=className;if(text!==undefined)n.textContent=text;return n;};
  const link=(label,url,className)=>{const a=el('a',className,label);a.href=Catalog.safeUrl(url);a.target='_blank';a.rel='noopener noreferrer';return a;};
  function toast(message){$('toast').textContent=message;$('toast').classList.add('visible');clearTimeout(toastTimer);toastTimer=setTimeout(()=>$('toast').classList.remove('visible'),2600);}
  function selected(){return Catalog.filterItems(items,{...state,featuredOnly:state.view==='featured',favoritesOnly:state.view==='favorites',favorites});}
  function favoriteButton(item){const b=el('button','favorite-button',favorites.has(item.id)?'★':'☆');b.type='button';b.setAttribute('aria-label',(favorites.has(item.id)?'取消收藏：':'收藏：')+item.name);b.setAttribute('aria-pressed',String(favorites.has(item.id)));b.addEventListener('click',()=>{
    const add=!favorites.has(item.id);if(add)favorites.add(item.id);else favorites.delete(item.id);
    try{localStorage.setItem('motion-index-favorites',JSON.stringify([...favorites]));}catch{storageAvailable=false;}
    toast(storageAvailable?(add?'已加入收藏':'已取消收藏'):'已更新本次收藏；浏览器无法持久保存，请导出备份');
    if(state.view==='favorites')render();else{b.textContent=add?'★':'☆';b.setAttribute('aria-pressed',String(add));b.setAttribute('aria-label',(add?'取消收藏：':'收藏：')+item.name);$('nav-favorites').textContent=favorites.size;}
  });return b;}
  function card(item){
    const node=el('article','card');node.dataset.id=item.id;
    const visual=el('div','card-visual');const cover=el('div','fallback-cover');
    const colors=['#355640','#514632','#3c425c','#5b3e33','#435735'];cover.style.setProperty('--cover',colors[parseInt(item.id.slice(-2),16)%colors.length]);
    cover.append(el('span','',item.category),el('strong','',item.name));visual.append(cover);
    if(state.previews && Catalog.safeUrl(item.thumbnail_url)){
      const img=el('img');img.alt=item.name+' — 原站提供的封面';img.loading='lazy';img.decoding='async';img.referrerPolicy='no-referrer';img.src=Catalog.safeUrl(item.thumbnail_url);img.addEventListener('error',()=>img.remove(),{once:true});visual.append(img);
    }
    visual.append(el('span','visual-label',item.kind==='视频'?'▶ 视频参考':item.category),favoriteButton(item));
    const body=el('div','card-body');const meta=el('div','card-meta');meta.append(el('span','',item.platform));
    if(item.featured)meta.append(el('span','featured-tag','✦ 精选'));if(item.repo_url)meta.append(el('span','','· 有源码入口'));
    if(/第三方索引|索引描述/.test(item.verification))meta.append(el('span','','· 索引线索'));
    body.append(meta,el('h3','',item.name),el('p','card-description',item.description));
    const tags=el('div','tags');(item.tags||[]).slice(0,3).forEach(t=>tags.append(el('span','tag',t)));body.append(tags);
    const actions=el('div','card-actions');actions.append(link(item.kind==='视频'?'观看原视频 ↗':'打开灵感 ↗',item.url,'open-link'));
    if(item.repo_url)actions.append(link('源码',item.repo_url,'source-link'));
    const details=el('button','','详情');details.type='button';details.setAttribute('aria-label','查看详情：'+item.name);details.addEventListener('click',()=>showDetail(item));actions.append(details);body.append(actions);node.append(visual,body);return node;
  }
  function showDetail(item){
    const b=$('detail-body');b.replaceChildren();b.append(el('p','eyebrow',item.platform+' / '+item.category));const h=el('h2','',item.name);h.id='detail-title';b.append(h,el('p','',item.description));
    const dl=el('dl');
    for(const [label,value] of [['作者',item.author],['原始标题',item.official_title],['参考关键词',(item.tags||[]).join(' / ')],['核验范围',item.verification],['核验日期',item.checked_at],['访问说明',item.access_notes],['许可记录',item.license_note||item.reuse_notes||'作品用于视觉参考；实际复用请核对原作者许可。']]){
      if(value)dl.append(el('dt','',label),el('dd','',value));
    }
    if(item.evidence_url){dl.append(el('dt','','资料来源'));const dd=el('dd');dd.append(link('打开核验来源 ↗',item.evidence_url));dl.append(dd);}
    b.append(dl);const actions=el('div','detail-actions');actions.append(link('打开原作品 ↗',item.url));if(item.repo_url)actions.append(link('查看源码 ↗',item.repo_url));b.append(actions);$('detail').showModal();
  }
  function render(){
    const list=selected();$('results').replaceChildren(...list.slice(0,state.limit).map(card));
    $('result-count').textContent=list.length+' 条灵感'+(state.category?' · '+state.category:'')+(state.platform==='GitHub'?' · 含独立演示页的 GitHub 源码入口':'');
    $('collection-title').textContent=state.view==='favorites'?'我的收藏':state.view==='featured'?'编辑精选':state.category||'发现灵感';
    $('empty').hidden=list.length!==0;$('empty-message').textContent=state.view==='favorites'?'点击卡片右上角的星标，把喜欢的作品留在这里。':'试试其他关键词，或重置筛选。';
    $('load-more').hidden=list.length<=state.limit;$('reset').hidden=!(state.query||state.category||state.platform||state.kind||state.view!=='all');
    $('nav-total').textContent=items.length;$('nav-favorites').textContent=favorites.size;
    document.querySelectorAll('[data-view]').forEach(b=>{b.classList.toggle('active',b.dataset.view===state.view);b.setAttribute('aria-pressed',String(b.dataset.view===state.view));});
    document.querySelectorAll('[data-category]').forEach(b=>{b.classList.toggle('active',b.dataset.category===state.category);b.setAttribute('aria-pressed',String(b.dataset.category===state.category));});
  }
  function reset(){Object.assign(state,{query:'',category:'',platform:'',kind:'',view:'all',limit:30});$('search').value='';$('platform').value='';$('kind').value='';render();}
  const counts=Object.entries(data.counts).sort((a,b)=>b[1]-a[1]);
  for(const [category,count] of [['',items.length],...counts]){const b=el('button','category-item');b.type='button';b.dataset.category=category;b.append(el('span','',category||'所有分类'),el('small','',count));b.addEventListener('click',()=>{state.category=category;state.limit=30;render();});$('categories').append(b);}
  for(const [value,label] of [[items.length,'精选资源'],[counts.length,'效果分类'],[items.filter(x=>x.kind==='视频').length,'展示视频'],[items.filter(x=>x.repo_url).length,'源码入口']]){const s=el('div','stat');s.append(el('strong','',value),el('span','',label));$('stats').append(s);}
  $('updated').textContent='整理于 '+data.updated_at;
  document.querySelectorAll('[data-view]').forEach(b=>b.addEventListener('click',()=>{state.view=b.dataset.view;state.limit=30;render();}));
  $('search').addEventListener('input',e=>{state.query=e.target.value;state.limit=30;render();});
  ['platform','kind'].forEach(key=>$(key).addEventListener('change',e=>{state[key]=e.target.value;state.limit=30;render();}));
  $('previews').addEventListener('change',e=>{state.previews=e.target.checked;render();});
  $('reset').addEventListener('click',reset);$('empty-reset').addEventListener('click',reset);
  $('load-more').addEventListener('click',()=>{state.limit+=30;render();});
  $('random').addEventListener('click',()=>{const list=selected();if(!list.length)return toast('当前没有结果，先调整筛选');showDetail(list[Math.floor(Math.random()*list.length)]);});
  $('close-detail').addEventListener('click',()=>$('detail').close());
  $('detail').addEventListener('click',e=>{if(e.target===$('detail')){const r=$('detail').getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)$('detail').close();}});
  $('export').addEventListener('click',()=>{const result=selected();const blob=new Blob([JSON.stringify({exported_at:new Date().toISOString(),items:result},null,2)],{type:'application/json;charset=utf-8'});const u=URL.createObjectURL(blob);const a=el('a');a.href=u;a.download='motion-index-'+(state.view==='favorites'?'favorites':'selection')+'.json';document.body.append(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(u),1000);toast('已导出 '+result.length+' 条结果');});
  document.addEventListener('keydown',e=>{if(e.key==='/'&&!['INPUT','TEXTAREA','SELECT'].includes(document.activeElement.tagName)&&!$('detail').open){e.preventDefault();$('search').focus();}});
  render();
})();
