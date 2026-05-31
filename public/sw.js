/* ============================================ */
/* Republic of Nauru — Service Worker v2        */
/* ============================================ */

const CACHE_NAME = 'nauru-v2';

const PRECACHE_URLS = [
  '/',
  '/favicon.svg',
  '/favicon.ico',
  '/site.webmanifest',
  '/offline.html'
];

// Static file extensions to cache-first
const STATIC_EXTENSIONS = /\.(css|js|mjs|woff2?|ttf|otf|eot|svg|png|jpg|jpeg|gif|webp|avif|ico|webmanifest)$/i;

// News & API routes — network-first (stale-while-revalidate fallback)
const NEWS_PATHS = /^\/(na\/)?news\//i;

// Install: precache critical assets
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => cache.addAll(PRECACHE_URLS))
      .then(() => self.skipWaiting())
  );
});

// Activate: remove old caches, take control immediately
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys
          .filter((key) => key !== CACHE_NAME)
          .map((key) => caches.delete(key))
      )
    ).then(() => self.clients.claim())
  );
});

// ---- Helper: cache-first with network fallback ----
function cacheFirst(request) {
  return caches.match(request).then((cached) => {
    if (cached) return cached;
    return fetchAndCache(request);
  });
}

// ---- Helper: network-first with cache fallback ----
function networkFirst(request) {
  return fetch(request)
    .then((response) => {
      if (response.ok) {
        const clone = response.clone();
        caches.open(CACHE_NAME).then((cache) => cache.put(request, clone));
      }
      return response;
    })
    .catch(() => caches.match(request));
}

// ---- Helper: fetch and cache response ----
function fetchAndCache(request) {
  return fetch(request).then((response) => {
    if (response.ok) {
      const clone = response.clone();
      caches.open(CACHE_NAME).then((cache) => cache.put(request, clone));
    }
    return response;
  });
}

// ---- Helper: serve offline fallback ----
function offlineFallback() {
  return caches.match('/offline.html');
}

// ---- Fetch handler ----
self.addEventListener('fetch', (event) => {
  const { request } = event;
  const url = new URL(request.url);

  // Only handle GET requests from our own origin
  if (request.method !== 'GET') return;

  // ---- External / cross-origin requests: let browser handle ----
  if (url.origin !== self.location.origin) return;

  // ---- 1) Static assets (CSS, JS, fonts, images): cache-first ----
  if (STATIC_EXTENSIONS.test(url.pathname)) {
    event.respondWith(cacheFirst(request));
    return;
  }

  // ---- 2) News / API routes: network-first ----
  if (NEWS_PATHS.test(url.pathname)) {
    event.respondWith(networkFirst(request));
    return;
  }

  // ---- 3) HTML / Navigation requests: network-first with offline fallback ----
  if (request.mode === 'navigate' ||
      request.headers.get('Accept')?.includes('text/html')) {
    event.respondWith(
      fetch(request)
        .then((response) => {
          const clone = response.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(request, clone));
          return response;
        })
        .catch(() =>
          caches.match(request).then((cached) => cached || offlineFallback())
        )
    );
    return;
  }

  // ---- 4) Everything else: cache-first ----
  event.respondWith(cacheFirst(request));
});
