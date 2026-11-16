const C='sc-v7',A=['./','index.html','manifest.json','assets/logo.png','assets/icon-192.png','assets/icon-512.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(C).then(c=>Promise.all(A.map(u=>c.add(u).catch(()=>{})))));self.skipWaiting()});
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x))))));
self.addEventListener('fetch',e=>{const u=new URL(e.request.url);
 if(u.origin!==location.origin||u.pathname.includes('/downloads/'))return;
 e.respondWith(fetch(e.request).catch(()=>caches.match(e.request)))});
