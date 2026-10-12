// La Finca Pastoreo: network-first app shell so it opens even with weak signal in the field.
const C="lafinca-v8";
self.addEventListener("install",e=>{ self.skipWaiting(); e.waitUntil(caches.open(C).then(c=>c.addAll(["./","./index.html","./manifest.webmanifest","./icon-192.png","./icon-512.png"]).catch(()=>{}))); });
self.addEventListener("activate",e=>{ e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==C).map(k=>caches.delete(k)))).then(()=>self.clients.claim())); });
self.addEventListener("fetch",e=>{ const r=e.request; if(r.method!=="GET") return; const u=new URL(r.url);
  if(u.origin!==location.origin){ return; }
  e.respondWith((r.mode==="navigate"?fetch(r.url,{cache:"no-cache",credentials:"same-origin"}):fetch(r)).then(res=>{ if(res.ok){ const cp=res.clone(); caches.open(C).then(c=>c.put(r,cp)); } return res; })
    .catch(()=>caches.match(r).then(m=>m||(r.mode==="navigate"?caches.match(u.pathname.startsWith("/live")?"/live/":"./index.html"):Response.error())))); });
