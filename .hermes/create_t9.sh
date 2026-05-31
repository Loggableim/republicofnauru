#!/bin/bash
cd /e/nauru
export HERMES_KANBAN_BOARD=nauru-content
export PYTHONPATH=cids-hermes-agent

python -m hermes_cli.main kanban create "T9 - Build, QA, Commit + Push" \
  --assignee integrator \
  --parent t_6b292b00 --parent t_cfd38c75 --parent t_8ceb3bcd \
  --parent t_4ba7c7e0 --parent t_2b2fd33a --parent t_b6dc75b3 --parent t_b3ea13ea \
  --body "PROJEKT-PFAD: /e/nauru
--
AUFGABE: Sprint Abschluss - Build testen, QA, Commit + Push.
WARTET AUF: T1-T7 (Content + SEO + PWA + Media)

WAS ZU TUN IST:
1. cd /e/nauru && npm run build - muss 63+ Pages liefern
2. Pruefe dist/ auf Vollstaendigkeit
3. git add -A
4. git commit -m \"[sprint] Phase 1: Content Upgrade + SEO + PWA + Media\"
5. git push origin master

AKZEPTANZKRITERIEN:
- Build erfolgreich (63+ pages)
- Git-Commit mit strukturierter Nachricht
- Keine broken files" \
  --json 2>&1
