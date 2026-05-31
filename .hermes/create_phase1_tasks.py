#!/usr/bin/env python
"""Create Phase 1 sprint tasks on nauru-content board."""
import subprocess, json, sys, os

BASE = "E:/nauru"
BOARD = "nauru-content"
ENV = {**os.environ, "HERMES_KANBAN_BOARD": BOARD, "PYTHONPATH": "cids-hermes-agent"}

def kanban(*args):
    """Call kanban CLI and return parsed JSON or None."""
    r = subprocess.run(
        ["python", "-m", "hermes_cli.main", "kanban", *args],
        capture_output=True, text=True, timeout=30, cwd=BASE, env=ENV
    )
    stdout = r.stdout.strip()
    if r.returncode != 0:
        print(f"  ERR: {r.stderr[:200]}", file=sys.stderr)
        return None
    if stdout and stdout.startswith("{"):
        try:
            return json.loads(stdout)
        except json.JSONDecodeError:
            pass
    return stdout

# ============================================================
# LANE A — Content Fill (content-filler)
# ============================================================
print("=== LANE A: Content Fill ===")

t1 = kanban("create", "T1 – About-Seiten Content Upgrade",
    "--assignee", "content-filler",
    "--body", "PROJEKT-PFAD: /e/nauru\n--\nAUFGABE: Jede About-Unterseite auf 500+ Wörter bringen mit faktenbasierten Inhalten.\n\nBETROFFENE DATEIEN:\n- src/pages/about/history.astro\n- src/pages/about/culture.astro\n- src/pages/about/the-people.astro\n- src/pages/about/economy.astro\n- src/pages/about/national-days.astro\n- src/pages/about/our-country.astro\n\nWAS ZU TUN IST:\n1. Jede Seite auf faktenbasierte 500+ Wörter bringen\n2. Quellen: nauru.gov.nr, existing JSON data in src/data/\n3. Strukturierte Abschnitte mit Zwischenüberschriften\n4. Fakten checken — NICHTS halluzinieren über Nauru\n\nAKZEPTANZKRITERIEN:\n- Alle 6 Seiten haben 500+ Wörter\n- Build läuft durch\n- Keine Faktenfehler (nur aus bestehenden Quellen)",
    "--json")
print(f"  T1: {t1}")

t2 = kanban("create", "T2 – Visit-Seiten Content Upgrade",
    "--assignee", "content-filler",
    "--body", "PROJEKT-PFAD: /e/nauru\n--\nAUFGABE: Visit-Seiten mit detaillierten, praktischen Reiseinformationen anreichern.\n\nBETROFFENE DATEIEN:\n- src/pages/visit/accommodation.astro\n- src/pages/visit/transport.astro\n- src/pages/visit/weather.astro\n- src/pages/visit/currency.astro\n- src/pages/visit/attire.astro\n- src/pages/visit/communications.astro\n\nWAS ZU TUN IST:\n1. accommodation: Preisspannen, Kontaktdaten, Buchungsinfos\n2. transport: Flugverbindungen, Mietwagen, Insel-Transport\n3. weather: Monats-Klimatabelle, beste Reisezeit\n4. currency: AUD, Banken, Kartenzahlung, Bargeld\n5. attire: Kleiderordnung, Packliste pro Saison\n6. communications: SIM-Karten, Roaming, Internet\n\nAKZEPTANZKRITERIEN:\n- Alle Seiten strukturiert mit Zwischenüberschriften\n- Praktische, reisetaugliche Informationen\n- Build läuft durch",
    "--json")
print(f"  T2: {t2}")

t3 = kanban("create", "T3 – Services-Seiten polish",
    "--assignee", "content-filler",
    "--body", "PROJEKT-PFAD: /e/nauru\n--\nAUFGABE: Services-Detailseiten mit Checklisten, Antragsinfos und Next-Steps anreichern.\n\nBETROFFENE DATEIEN:\n- src/pages/services/citizenship.astro\n- src/pages/services/education.astro\n- src/pages/services/health.astro\n- src/pages/services/immigration.astro\n- src/pages/services/index.astro\n\nWAS ZU TUN IST:\n1. citizenship: Voraussetzungen, Antragsweg, Kosten\n2. education: Schulsystem, Stipendien, Internationale Programme\n3. health: Krankenhaus, Apotheken, Notruf\n4. immigration: Visum-Arten, Aufenthalt, Arbeitserlaubnis\n5. services/index: Übersicht verbessern\n\nAKZEPTANZKRITERIEN:\n- Jede Seite hat praktische Checkliste\n- Build läuft durch",
    "--json")
print(f"  T3: {t3}")

# ============================================================
# LANE B — SEO & Structure (seo-architect)
# ============================================================
print("\n=== LANE B: SEO & Structure ===")

t4 = kanban("create", "T4 – Schema.org Structured Data",
    "--assignee", "seo-architect",
    "--body", "PROJEKT-PFAD: /e/nauru\n--\nAUFGABE: JSON-LD Structured Data auf ALLEN Seiten einbauen.\n\nBETROFFENE DATEIEN:\n- src/layouts/BaseLayout.astro (global)\n- src/layouts/SubpageLayout.astro (per-page)\n\nWAS ZU TUN IST:\n1. Organization Schema mit Logo, Name, URL, social profiles\n2. BreadcrumbList auf jeder Subpage (dynamisch aus path)\n3. Article Schema auf News-Seiten\n4. WebPage Schema auf Content-Seiten\n5. FAQPage Schema auf Services/Visit-Seiten mit Fragen\n\nAKZEPTANZKRITERIEN:\n- Validiert im Google Rich Results Test\n- Kein doppeltes Schema\n- Build läuft durch",
    "--json")
print(f"  T4: {t4}")

t5 = kanban("create", "T5 – Meta-Tags + OG für alle Subpages",
    "--assignee", "seo-architect",
    "--body", "PROJEKT-PFAD: /e/nauru\n--\nAUFGABE: Fehlende Meta-Title, Meta-Description und OpenGraph-Tags auf allen Subpages ergänzen.\n\nBETROFFENE DATEIEN:\n- src/layouts/BaseLayout.astro\n- src/layouts/SubpageLayout.astro\n- src/pages/**/*.astro (alle Einzelseiten)\n\nWAS ZU TUN IST:\n1. Jede Seite bekommt unique meta title + description\n2. OG:title, OG:description, OG:image, OG:url auf jeder Seite\n3. Falls kein OG-Image existiert: AI-generiertes Default-Image\n4. Twitter Card Tags (summary_large_image)\n\nAKZEPTANZKRITERIEN:\n- Keine Seite ohne unique meta description\n- Build läuft durch",
    "--json")
print(f"  T5: {t5}")

# ============================================================
# LANE C — Infrastructure (frontend-dev)
# ============================================================
print("\n=== LANE C: Infrastructure ===")

t6 = kanban("create", "T6 – PWA + Performance + A11y Hardening",
    "--assignee", "frontend-dev",
    "--body", "PROJEKT-PFAD: /e/nauru\n--\nAUFGABE: PWA verbessern, Service Worker optimieren, Performance/Accessibility ausbauen.\n\nWAS ZU TUN IST:\n1. sw.js: cache-first für statics, network-first für news, offline fallback page\n2. manifest.json: prüfen auf Vollständigkeit (icons, theme_color, display, scope)\n3. BaseLayout.astro: <link rel='preload'> für kritische Fonts, async/defer für non-critical JS\n4. skip-to-content link funktioniert auf allen Seiten\n5. :focus-visible styles auf allen interaktiven Elementen\n6. src/data/a11y.json: accessibility statement (optional)\n\nAKZEPTANZKRITERIEN:\n- Lighthouse Performance >= 90\n- Lighthouse A11y >= 95\n- Service Worker registriert ohne Fehler\n- Build läuft durch",
    "--json")
print(f"  T6: {t6}")

# ============================================================
# LANE D — NA Translation Recovery (frontend-dev)
# ============================================================
print("\n=== LANE D: NA Translation Recovery ===")

t7 = kanban("create", "T7 – NA Translation: Fix Blocked Tasks",
    "--assignee", "frontend-dev",
    "--body", "PROJEKT-PFAD: /e/nauru\n--\nAUFGABE: Die 16 blocked NA-Translation Tasks identifizieren und fixen.\n\nPRÜFEN:\n1. HERMES_KANBAN_BOARD=nauru-translation kanban list --json — prüfe Status aller Tasks\n2. Für jeden blocked Task: kanban show <id> — lies Block-Grund\n3. Kategorisiere: review-required? crashed? iteration-budget?\n4. Reclaim oder complete pro Task\n\nAKTUELLER STAND:\n- nauru-translation board hat 16 Tasks, alle blocked\n- Alle assigned an frontend-dev\n- Dispatcher läuft unter na-translation-kanban-dispatcher\n\nAKZEPTANZKRITERIEN:\n- Alle NA-Translation Tasks entweder done oder mit klarem Grund blocked\n- Restliche Build-fähige Arbeit committed",
    "--json")
print(f"  T7: {t7}")

# ============================================================
# LANE E — Media & Design (feat-builder, later phase)
# ============================================================
print("\n=== LANE E: Media & Design ===")

t8 = kanban("create", "T8 – OG-Image + Hero-Bild generieren",
    "--assignee", "feat-builder",
    "--body", "PROJEKT-PFAD: /e/nauru\n--\nAUFGABE: Fehlende visuelle Assets erstellen.\n\nWAS ZU TUN IST:\n1. public/og-image.svg — OG-Image 1200×630 mit Nauru-Flaggen-Farben + Text\n   - Navy (#002B7F) Hintergrund\n   - Gelb (#FFC72C) Akzente\n   - 'Republic of Nauru' Titel\n2. public/hero-nauru.jpg — AI-generiertes Hero-Bild (Nauru-Landschaft)\n   - Verwende image_generate tool mit passendem Prompt\n   - WebP Format, optimiert\n3. public/favicon.svg — prüfen ob vorhanden, ggf. verbessern\n\nAKZEPTANZKRITERIEN:\n- OG-Image valid (1200×630, <100KB)\n- Hero-Bild responsiv\n- Build läuft durch",
    "--json")
print(f"  T8: {t8}")

# ============================================================
# SYNTHESIS (integrator)
# ============================================================
print("\n=== SYNTHESIS ===")

t9 = kanban("create", "T9 – Build, QA, Commit & Push",
    "--assignee", "integrator",
    "--parent", t1 if t1 and "t_" in str(t1) else "",
    "--parent", t2 if t2 and "t_" in str(t2) else "",
    "--parent", t3 if t3 and "t_" in str(t3) else "",
    "--parent", t4 if t4 and "t_" in str(t4) else "",
    "--parent", t5 if t5 and "t_" in str(t5) else "",
    "--parent", t6 if t6 and "t_" in str(t6) else "",
    "--parent", t8 if t8 and "t_" in str(t8) else "",
    "--body", "PROJEKT-PFAD: /e/nauru\n--\nAUFGABE: Sprint Abschluss — Build testen, QA, Commit & Push.\n\nWARTET AUF: T1 (About Content), T2 (Visit Content), T3 (Services Content),\nT4 (Schema.org), T5 (Meta/OG), T6 (PWA/A11y), T8 (Media)\n\nWAS ZU TUN IST:\n1. cd /e/nauru && npm run build — muss 63+ Pages liefern\n2. Prüfe dist/ auf Vollständigkeit\n3. git add -A && git commit -m \"[sprint] Phase 1: Content + SEO + PWA + Media\"\n4. git push origin master\n\nAKZEPTANZKRITERIEN:\n- Build erfolgreich (63+ pages)\n- Git-Commit mit strukturierter Nachricht\n- Keine broken files",
    "--json")
print(f"  T9: {t9}")

# ============================================================
# Summary
# ============================================================
print("\n" + "=" * 50)
print("ERSTELLTE TASKS:")
print(f"  T1: {t1}")
print(f"  T2: {t2}")
print(f"  T3: {t3}")
print(f"  T4: {t4}")
print(f"  T5: {t5}")
print(f"  T6: {t6}")
print(f"  T7: {t7}")
print(f"  T8: {t8}")
print(f"  T9: {t9}")
print("=" * 50)

# Verify
r = subprocess.run(
    ["python", "-m", "hermes_cli.main", "kanban", "stats", "--json"],
    capture_output=True, text=True, timeout=15, cwd=BASE, env=ENV
)
if r.returncode == 0:
    print("\nBOARD STATUS:")
    print(r.stdout)
