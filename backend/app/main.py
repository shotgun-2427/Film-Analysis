from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from app.db.database import Base, engine, SessionLocal
from app.models import Match, SetPiece, Corner, Penalty
from app.services.penalty_analytics import PenaltyAnalyticsService
Base.metadata.create_all(engine)
app=FastAPI(title="Wisconsin Soccer Analytics API",version="0.1.0")
app.add_middleware(CORSMiddleware,allow_origins=["http://localhost:5173"],allow_methods=["*"],allow_headers=["*"])
def dump(x): return {c.name:getattr(x,c.name) for c in x.__table__.columns}
@app.get("/api/health")
def health(): return {"status":"ok","coordinate_system":"105m x 68m"}
@app.get("/api/matches")
def matches():
    with SessionLocal() as db: return [dump(x) for x in db.scalars(select(Match)).all()]
@app.get("/api/matches/{match_id}")
def match(match_id:int):
    with SessionLocal() as db:
        item=db.get(Match,match_id)
        if not item: raise HTTPException(404,"Match not found")
        return dump(item)
@app.get("/api/set-pieces")
def set_pieces(match_id:int|None=None):
    with SessionLocal() as db:
        q=select(SetPiece); q=q.where(SetPiece.match_id==match_id) if match_id else q
        return [dump(x) for x in db.scalars(q).all()]
@app.get("/api/analytics/penalties")
def penalty_analytics():
    with SessionLocal() as db:
        rows=db.scalars(select(Penalty)).all(); goals=sum(x.outcome=="goal" for x in rows)
        return PenaltyAnalyticsService.get_smoothed_conversion_rate(goals,len(rows))
