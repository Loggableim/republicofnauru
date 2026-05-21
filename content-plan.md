# 📋 Content Plan — republicofnauru.com

> Basierend auf Analyse von nauru.gov.nr, gescrapten PDFs (2019–2025) und bestehenden JSON-Daten
> Stand: 21. Mai 2026

---

## 🧭 Sitemap (geplant)

```
republicofnauru.com/
├── /                               # Homepage (V4 Hybrid — fertig)
├── /about/                         # Über Nauru
│   ├── /about/our-country          # Geographie & Lage
│   ├── /about/history              # Geschichte (Timeline → ausführlich)
│   ├── /about/the-people           # 12 Stämme, Bevölkerung, Sprache
│   ├── /about/culture              # Tanz, Musik, Feste, Küche
│   ├── /about/economy              # Phosphat, Fischerei, Zukunft
│   └── /about/national-days        # Angam Day, Constitution Day
├── /visit/                         # Reiseplanung
│   ├── /visit/visa                 # Visum (gescrapt ✓)
│   ├── /visit/accommodation        # Hotels & Unterkünfte
│   ├── /visit/transport            # Flüge, Mietwagen, Infrastruktur
│   ├── /visit/weather              # Klima & beste Reisezeit
│   ├── /visit/currency             # AUD, Banken, Karten
│   ├── /visit/attire               # Kleiderordnung
│   └── /visit/communications       # Internet, SIM-Karten, Telefon
├── /news/                          # Aktuelle Nachrichten
│   └── /news/[...slug]             # Einzelartikel (dynamisch)
├── /services/                      # Bürger- & Besucher-Services
│   ├── /services/passports         # Pass & Visa
│   ├── /services/business          # Firmengründung
│   ├── /services/education         # Schulen & Stipendien
│   ├── /services/healthcare        # Medizinische Versorgung
│   ├── /services/housing           # Wohnen & Land
│   ├── /services/legal             # Justiz & Gesetze
│   ├── /services/environment       # Klima & Umweltschutz
│   └── /services/transport         # Verkehr & Infrastruktur
├── /directory/                     # Kontakt-Verzeichnis
│   ├── /directory/presidents-office
│   ├── /directory/ministry-finance
│   ├── /directory/ministry-education
│   └── /directory/ministry-environment
├── /contact/                       # Kontakt & Anfragen
└── /resources/                     # Downloads & Links
    ├── /resources/bulletins        # Nauru Bulletin (2019–2025)
    ├── /resources/directory        # Government Directory (PDF)
    └── /resources/constitution     # Verfassung (PDF)
```

---

## 📦 Content-Quellen

| Quelle | Art | Nutzbar für |
|--------|-----|-------------|
| **nauru.gov.nr (scraped)** | Live-HTML | News, Struktur, Kontaktdaten |
| **Government Directory 2025** | PDF | /directory/ |
| **Nauru Bulletin 2019–2025** | PDFs (7 Jg.) | /resources/bulletins |
| **Visa Requirements** | PDF | /visit/visa |
| **Constitution** | PDF | /resources/constitution |
| **Eigene Recherche** | Sekundär | Tourismus, Kultur, Geschichte |
| **Unsere JSON-Daten** | Fertig | Startseite (11 Sections) |

---

## 🎯 Phase 1 — Foundation (JETZT)

> **Priorität:** Alle Daten existieren, nur noch in Astro-Pages umsetzen

| Page | Component(s) | Daten-Status | Aufwand |
|------|-------------|-------------|---------|
| **/** (Home) | 11 Components | ✅ Fertig | Läuft |
| **/about/history** | TimelineSection extended | ✅ timeline.json fertig | 1h |
| **/about/culture** | CultureSection extended | ✅ culture.json fertig | 1h |
| **/news** | NewsSection + Pagination | ✅ news.json, PDF-Archive | 2h |
| **/directory** | DirectorySection extended | ✅ directory.json + PDF | 1h |
| **/contact** | ContactSection | ✅ contact.json fertig | 0.5h |
| **/services** | ServicesSection extended | ✅ services.json fertig | 0.5h |

**Gesamt Phase 1:** ~6h → 8 statische Unterseiten

---

## 📄 Phase 2 — Content Pages (NÄCHSTE)

> **Priorität:** Inhalte müssen recherchiert/getextet werden

| Page | Content-Quelle | Neuer Content? | Aufwand |
|------|---------------|---------------|---------|
| **/about/our-country** | nauru.gov.nr + Wikipedia | ✓ Überarbeitung | 2h |
| **/about/the-people** | nauru.gov.nr (12 Tribes) | ✓ Anreicherung | 2h |
| **/about/economy** | nauru.gov.nr + PDFs | ✓ Update nötig | 2h |
| **/about/national-days** | nauru.gov.nr | ✓ Aufbereitung | 1h |
| **/visit/visa** | PDF gescrapt ✅ | Kleine Anpassung | 1h |
| **/visit/accommodation** | nauru.gov.nr + Recherche | ✓ Fast komplett neu | 2h |
| **/visit/transport** | nauru.gov.nr + Recherche | ✓ Mix | 1.5h |
| **/visit/weather** | Klimadaten | ✓ Leicht | 0.5h |
| **/visit/currency** | nauru.gov.nr | ✓ Update | 0.5h |
| **/visit/attire** | nauru.gov.nr | ✓ Copy-Edit | 0.5h |
| **/visit/communications** | nauru.gov.nr | ✓ Minimal | 0.5h |

**Gesamt Phase 2:** ~13.5h → 11 Content-Seiten

---

## 🖼️ Phase 3 — Media & Design (SOBALD WIE MÖGLICH)

| Element | Status | Priorität |
|---------|--------|-----------|
| **Hero-Bild (Nauru-Landschaft)** | ❌ Fehlt | 🔴 Hoch |
| **News-Thumbnails** | ❌ Nur Emoji-Platzhalter | 🟡 Mittel |
| **Karte (OpenStreetMap/Leaflet)** | ❌ Fehlt | 🟡 Mittel |
| **Foto-Galerie** | ❌ Fehlt | 🟢 Niedrig |
| **Social-Media-Profile** | ❌ Keine echten Links | 🟢 Niedrig |

---

## 📊 Media-Bestand (gescrapte PDFs)

```
📁 scraped-site/media-files/
├── 📄 visa-requirements.pdf          ← RELEVANT für /visit/visa
├── 📄 nauru-constitution.pdf         ← RELEVANT für /resources/constitution
├── 📄 government-directory-2025.pdf   ← RELEVANT für /directory
├── 📄 lorem_ipsum_generator.pdf      ← PLATZHALTER (ignorieren)
├── 📄 nauru-bulletin/
│   ├── 2019.pdf
│   ├── 2020.pdf
│   ├── 2021.pdf
│   ├── 2022.pdf
│   ├── 2023.pdf
│   ├── 2024.pdf
│   ├── 2025.pdf
│   └── [undated].pdf
│   → RELEVANT für /resources/bulletins
```

---

## 🔤 Sprachstrategie

| Sprache | Umfang | Priorität |
|---------|--------|-----------|
| **🇬🇧 Englisch** | 100% der Seite | 🔴 Phase 1 |
| **🇳🇷 Nauruisch (Dorerin Naoero)** | Hero, TopBar, CTAs, Footer | 🟡 Phase 3 |
| **🇩🇪 Deutsch** | Tourismus-Seiten (optional) | 🟢 Phase 4 |

---

## 🏗️ Technische Umsetzung

```
# Astro-Routing-Struktur

src/pages/
├── index.astro                    # Home (fertig)
├── about/
│   ├── index.astro                # About-Übersicht
│   ├── our-country.astro
│   ├── history.astro              # Timeline ausbauen
│   ├── the-people.astro
│   ├── culture.astro              # Culture ausbauen
│   ├── economy.astro
│   └── national-days.astro
├── visit/
│   ├── index.astro                # Visit-Übersicht
│   ├── visa.astro
│   ├── accommodation.astro
│   ├── transport.astro
│   ├── weather.astro
│   ├── currency.astro
│   ├── attire.astro
│   └── communications.astro
├── news/
│   ├── index.astro                # News-Liste
│   └── [slug].astro               # Einzelartikel (getStaticPaths)
├── services/
│   ├── index.astro                # Services-Übersicht
│   └── [slug].astro               # Einzelseite (optional)
├── directory/
│   ├── index.astro                # Directory (fertig bis auf Routing)
│   └── [slug].astro               # Einzelkontakt (optional)
├── contact/
│   └── index.astro                # Kontakt (Content aus contact.json)
└── resources/
    ├── index.astro                # Download-Übersicht
    ├── bulletins.astro
    └── constitution.astro
```

---

## ⏱️ Roadmap

```
Woche 1 ═══════════════════════════════════════
  ████████░░░░░░░░░░░░░░░░░░  Phase 1 (8 Pages)
  - Home (✅ fertig)
  - Services (/services)
  - Directory (/directory)
  - Contact (/contact)
  - News (/news + /news/[slug])
  - Culture (/about/culture)
  - History (/about/history)

Woche 2 ═══════════════════════════════════════
  ████████████████░░░░░░░░░░  Phase 2 (11 Content Pages)
  - Our Country, The People
  - Economy, National Days
  - Alle 7 Visit-Pages

Woche 3 ═══════════════════════════════════════
  ████████████████████████░░  Phase 3 (Media)
  - Bilder, Karte, Galerie
  - Social-Media-Links
  - Hero-Update mit echten Fotos

Woche 4 ═══════════════════════════════════════
  ██████████████████████████  Deployment
  - Cloudflare Pages
  - Custom Domain (republicofnauru.com)
  - Cronjob für News-Updates
  - Nauruische Übersetzung (Start)
```

---

## ✅ Quick-Check: Was fehlt noch?

| Bereich | Status |
|---------|--------|
| 🏠 Homepage | ✅ Fertig (11 Sections) |
| 🗺️ Sitemap | 📋 Geplant |
| 📰 News-System | ⬜ Seiten fehlen (JSON existiert) |
| 📖 About-Seiten | ⬜ Content recherchiert, Pages fehlen |
| ✈️ Visit-Seiten | ⬜ PDFs gescrapt, Pages fehlen |
| 🛠️ Services-Seiten | ⬜ JSON existiert, Pages fehlen |
| 📞 Directory-Seiten | ⬜ JSON + PDF existieren |
| 🖼️ Bilder/Medien | ❌ Fehlt komplett |
| 🌐 Mehrsprachigkeit | ⬜ Geplant |
| 🚀 Deployment | ⬜ Cloudflare Pages |
| 📡 RSS-News-Import | ⬜ Geplant (Cronjob) |
| 📱 Mobile Optimierung | ✅ Fertig |
| 🎯 SEO | ⬜ Meta-Tags fehlen auf Unterseiten |

---

*Erstellt: 21. Mai 2026 · Basis: official-site-analysis.md + scraped-site + JSON-Data*
