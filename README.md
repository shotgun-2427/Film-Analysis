# Wisconsin Women's Soccer Analytics

A local-first research prototype joining film, pitch-coordinate reconstruction, structured set-piece annotation, descriptive statistics, and analyst-authored evidence. Corners and penalties are first-class modules beneath a shared set-piece model. All data is synthetic and labeled as demonstration data.

## Prerequisites

- Python 3.12+ (3.11 also works for development)
- Node.js 20+ and npm

## Install and run

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r backend/requirements.txt
python scripts/seed.py
cd backend && uvicorn app.main:app --reload --port 8000
```

In a second terminal:

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`; API docs are at `http://localhost:8000/docs`.

Root convenience commands are available through `make seed`, `make backend`, `make frontend`, and `make test`.

## Database initialization and demo data

`python scripts/seed.py` recreates `data/soccer.db` and loads Wisconsin, opponents, six matches, 40 players, 20 corners, 10 penalties, a five-kick shootout sequence, and findings. Coordinates use a 105 × 68-meter pitch; penalty endpoints retain continuous coordinates on the 7.32 × 2.44-meter goal.

## Tests and build

```bash
cd backend && pytest
cd frontend && npm run build
```

## Structure

- `backend/app/models`: SQLAlchemy domain model
- `backend/app/services`: spatial, corner, and penalty analysis
- `frontend/src/components`: layout and procedural React Three Fiber pitch
- `frontend/src/pages`: season, match, reconstruction, and penalty workspaces
- `data`: local SQLite database (generated)
- `scripts`: deterministic demo seed
- `docs`: implementation notes

## Architecture

Python owns persistence and statistical computation. React owns interaction and visualization. The reconstruction uses metric pitch coordinates and transforms them only at the Three.js boundary. Set pieces carry shared temporal/match context; corner and penalty tables carry their distinct geometry. The penalty service uses Beta-prior shrinkage and reports intervals and sample size rather than presenting tiny raw samples as certainty.

The video surface uses a local-provider placeholder; no Hudl scraping or assumed API exists. A production next step is a typed `VideoProvider` adapter, persistent keyframe editing API, real local film upload, richer migrations, and calibrated tracking imports. The MVP implements linear synthetic playback, camera presets, timeline seeking, continuous goal mapping, and synthetic demonstrations; video synchronization and draggable editor persistence remain extension work.
