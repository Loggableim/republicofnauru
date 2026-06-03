export interface AffiliateLink {
  title: string;
  description: string;
  url: string;
  category: string;
}

// Amazon affiliate tag
const tag = 'nova079-20';

// Helper to build Amazon links
export function amazonLink(asin: string): string {
  return `https://www.amazon.com/dp/${asin}?tag=${tag}`;
}

// Section-specific affiliate links
export const affiliateLinks: Record<string, AffiliateLink[]> = {
  about: [
    {
      title: 'Lonely Planet Pacific Islands',
      description: 'Comprehensive guide covering Nauru and other Pacific island nations.',
      url: amazonLink('1786576991'),
      category: 'Travel Guides',
    },
    {
      title: 'Pacific Island Nation Map',
      description: 'Detailed map of the central Pacific including Nauru.',
      url: amazonLink('1552128159'),
      category: 'Maps',
    },
  ],
  visit: [
    {
      title: 'Universal Travel Adapter',
      description: 'Compact worldwide power adapter compatible in Nauru and across the Pacific.',
      url: amazonLink('B09LB28G5X'),
      category: 'Travel Accessories',
    },
    {
      title: 'Packable Backpack 20L',
      description: 'Lightweight foldable daypack for island exploration.',
      url: amazonLink('B07CP84GFG'),
      category: 'Travel Accessories',
    },
  ],
  services: [
    {
      title: 'Document Organizer Wallet',
      description: 'Keep passports, visas, and travel documents safe and organized.',
      url: amazonLink('B07JW9Y7NL'),
      category: 'Travel Accessories',
    },
  ],
  directory: [
    {
      title: 'Emergency Whistle Keychain',
      description: 'Compact safety whistle for travel peace of mind.',
      url: amazonLink('B07KQXGHSL'),
      category: 'Safety',
    },
  ],
  culture: [
    {
      title: 'Pacific Islands: Environment & Society',
      description: 'In-depth exploration of Pacific Island cultures including Nauru.',
      url: amazonLink('0824889309'),
      category: 'Books',
    },
  ],
  history: [
    {
      title: 'The History of Nauru',
      description: 'A detailed account of Nauruan history from ancient times to independence.',
      url: amazonLink('982906801X'),
      category: 'Books',
    },
  ],
  news: [
    {
      title: 'The Pacific Island Economies',
      description: 'Understanding the economic landscape of Pacific island nations.',
      url: amazonLink('0824821135'),
      category: 'Books',
    },
  ],
  contact: [
    {
      title: 'Notebook & Pen Set',
      description: 'Essential journal for travel notes and planning.',
      url: amazonLink('B09QZGY6GY'),
      category: 'Stationery',
    },
  ],
  default: [
    {
      title: 'Pacific Islands Travel Guide',
      description: 'Essential guide for visitors to the Pacific Islands.',
      url: amazonLink('1786576991'),
      category: 'Travel Guides',
    },
  ],
};

export const amazonTag = tag;
