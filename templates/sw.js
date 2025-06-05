const CACHE_NAME = 'hashout-pwa-cache-v1';
const urlsToCache = [
    '/',
    // You'll need to add paths to your app's actual CSS/JS/images here.
    // For now, let's assume you'll create these later.
    // Example: '/static/myapp/css/style.css', if you put app CSS there.
    // Example: '/static/myapp/js/script.js', if you put app JS there.
    // '/static/images/icon-192x192.png',
    // '/static/images/icon-512x512.png',
    // '/static/images/maskable_icon.png',
    // '/static/manifest.json'
];

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                console.log('Opened cache');
                return cache.addAll(urlsToCache);
            })
    );
});

self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                if (response) {
                    return response;
                }
                return fetch(event.request);
            })
    );
});

self.addEventListener('activate', event => {
    const cacheWhitelist = [CACHE_NAME];
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (cacheWhitelist.indexOf(cacheName) === -1) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
});
