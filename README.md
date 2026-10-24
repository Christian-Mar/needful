# needful.

**Koop minder. Kies beter.**

Een beslissingshulp vóór je iets koopt. In ± 3 minuten beantwoord je vier eerlijke vragen en krijg je één onderbouwd advies: laten, lenen, huren, samen kopen, alternatief product, kopen & later doorverkopen, of bewust kopen.

Groepswerk **Python Developer 2** · Robin · Femke · Christian · oktober 2026

## De vier vragen

| # | Vraag | Wat we berekenen |
|---|-------|------------------|
| 1 | Heb je het écht nodig? | behoefte of impuls |
| 2 | Hoe vaak ga je het gebruiken? | kost per gebruik (€ ÷ aantal keer) |
| 3 | Kan het anders in jouw regio? | lenen · huren · tweedehands in de buurt |
| 4 | Hoe duurzaam is het product? | levensduur · herstelbaar · recycleerbaar · reviews → score /100 |

Antwoorden kan typend of met je stem. Geen login, geen persoonsgegevens.

## Stack

- **Python 3.12** via uv
- **NiceGUI** – frontend (desktop web + PWA voor Android/iPhone), draait op FastAPI
- **FastAPI + Pydantic** – API
- **SQLModel / SQLAlchemy 2 + Alembic** – database-laag
- **PostgreSQL** – admin-module (gebruik & verbruik) + cache regio × product
- **BeautifulSoup + httpx** – korte scraping van uitleen-/huur-/tweedehandssites
- **OpenRouter** (of Ollama lokaal) – LLM + spraakmodel
- **pytest** – tests, vooral op de rekenkern
- **Docker** – lokaal draaien in één commando

Bewust niet: Next.js/JavaScript, Streamlit, Django, LangChain.

## Projectstructuur

```
needful/            Python-package
  api/              FastAPI-routes
  flow/             vragen & volgorde
  calc/             €/gebruik · score · advies  (pure Python, volledig getest)
  alternatives/     LLM + scraping per regio
  voice/            spraak → antwoord
  db/               SQLModel-modellen, admin-module, cache
  ui/               NiceGUI-schermen + PWA (manifest, service worker)
tests/              pytest
docs/concept/       pitch & voorontwerp (pdf)
```

## Lokaal draaien

We gebruiken [uv](https://docs.astral.sh/uv/) voor Python en packages (eenmalig installeren):

```powershell
# Windows (PowerShell), daarna terminal opnieuw openen
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Dan in de projectmap:

```bash
cp .env.example .env            # Windows: copy .env.example .env
uv python install 3.12
uv sync --extra dev             # maakt .venv en installeert alles
uv run pytest                   # tests
uv run uvicorn needful.main:app --reload --port 8080
```

`uv run` gebruikt automatisch de .venv, je hoeft niets te activeren. Commit `uv.lock` mee zodat iedereen dezelfde versies heeft.

### Met Docker

Installeer [Docker Desktop](https://www.docker.com/products/docker-desktop/) en start het.

```bash
docker compose up --build       # Postgres + app samen (Ctrl+C om te stoppen)
docker compose up -d db         # alleen de database, app lokaal via uv run
docker compose down             # alles stoppen
```

App: http://localhost:8080 · API-docs: http://localhost:8080/docs

## Tests

```bash
uv run pytest
```

## Werkwijze

- 4 sprints van 30 uur (3 × 10 u.), MVP online na sprint 3, spraak in sprint 4.
- Claude Code schrijft het meeste code; wij plannen elke feature eerst samen, reviewen elke pull request en mergen niets wat niemand van ons begrijpt.
- Werken op een branch per feature (`feat/...`), pull request naar `main`, minstens één review.
- Issues/kanban: zie het Projects-tabblad van deze repo.

## Roadmap

| Sprint | Thema | Belangrijkste onderdelen |
|--------|-------|--------------------------|
| 1 | Fundament | vragen & scoremodel, design & frontend-basis, repo/Docker/db |
| 2 | Vragenflow | api + flow + calc + tests, NiceGUI-wizard |
| 3 | Advies & live | alternatives (LLM + scraping), PWA, admin-module, gebruikerstest, online |
| 4 | Spraak | spraakmodellen vergelijken + inbouwen, afwerking, buffer |

Bewust nog niet (versie 2): avatar · accounts & login · eigen ML-modellen · afkoel-wachtlijst.
