# Samenwerken

1. Maak voor elke feature een branch: `git checkout -b feat/korte-naam`
2. Plan de feature eerst samen (kort, in de WhatsApp of een issue).
3. Bouw ze (met Claude Code), schrijf tests voor alles in `needful/calc/`.
4. Open een pull request naar `main`; minstens één van de anderen reviewt.
5. We mergen niets wat niemand van ons begrijpt.

Voor je pusht: `ruff check . && pytest`
