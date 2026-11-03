(function(root){
  function safeUrl(value){
    try { const url = new URL(value); return ['http:','https:'].includes(url.protocol) && !url.username && !url.password ? url.href : ''; }
    catch { return ''; }
  }
  function filterItems(items, options={}){
    const terms = (options.query || '').toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);
    return items.filter(item=>{
      const haystack = [item.name,item.description,item.category,item.author,item.official_title,...(item.tags||[])].filter(Boolean).join(' ').toLocaleLowerCase();
      return terms.every(t=>haystack.includes(t))
        && (!options.category || item.category===options.category)
        && (!options.platform || (options.platform==='GitHub' ? !!item.repo_url || (item.url||'').includes('github.com/') : item.platform===options.platform))
        && (!options.kind || (options.kind==='视频' ? item.kind==='视频' : item.kind!=='视频'))
        && (!options.featuredOnly || item.featured)
        && (!options.favoritesOnly || (options.favorites||new Set()).has(item.id))
        && (!options.sourceOnly || !!item.repo_url);
    });
  }
  const api = {safeUrl,filterItems};
  if(typeof module!=='undefined' && module.exports) module.exports=api;
  else root.Catalog=api;
})(typeof globalThis!=='undefined'?globalThis:this);
