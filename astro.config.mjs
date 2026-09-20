// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://republicofnauru.com',
  trailingSlash: 'always',
  integrations: [sitemap({
    lastmod: new Date(),
    filter: (page) => {
      // Exclude NA locale pages (noindex)
      if (page.includes('/na/')) return false;
      // Exclude unverified news articles
      if (page.includes('/news/') && !page.endsWith('/news/')) {
        // Let news articles through — verification handled per-page via noindex meta
        // but we can filter at build time via the page content
        return true;
      }
      // Exclude affiliate-disclosure from sitemap (thin content)
      if (page.includes('/affiliate-disclosure/')) return false;
      return true;
    },
  })],
});
