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

// Section-specific affiliate links — only on travel/guide/relevant pages, NOT on sensitive pages
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
  guide: [
    {
      title: 'Schnorchelset für Erwachsene',
      description: 'Hochwertiges Tauchset mit Maske, Schnorchel und Flossen – ideal für die Korallenriffe Naurus.',
      url: amazonLink('B09QY6H8P2'),
      category: 'Travel Accessories',
    },
    {
      title: 'Wasserdichte Handyhülle',
      description: 'Schützt Ihr Smartphone beim Schnorcheln und an den Stränden Naurus vor Wasser und Sand.',
      url: amazonLink('B08D3Y5PFZ'),
      category: 'Travel Accessories',
    },
    {
      title: 'Universal Travel Adapter',
      description: 'Kompakter Weltreisestecker mit USB – kompatibel mit den Steckdosen auf Nauru.',
      url: amazonLink('B09LB28G5X'),
      category: 'Travel Accessories',
    },
    {
      title: 'Reiseführer Pazifische Inseln',
      description: 'Lonely Planet Pacific Islands – umfassender Guide für Nauru und die gesamte Pazifikregion.',
      url: amazonLink('1786576991'),
      category: 'Travel Guides',
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
