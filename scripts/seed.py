import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/"backend"))
from app.db.database import Base,engine,SessionLocal
from app.models import *
Base.metadata.drop_all(engine); Base.metadata.create_all(engine)
with SessionLocal() as db:
    teams=[Team(id=1,name="Wisconsin"),*[Team(id=i+2,name=n) for i,n in enumerate(["Notre Dame","BYU","UIC","Michigan"])]]; db.add_all(teams)
    matches=[("2026-08-20","Notre Dame","Alumni Stadium","Nonconference","W 2–1","Complete"),("2026-08-23","BYU","McClimon Track/Soccer Complex","Nonconference","W 1–0","Complete"),("2026-08-30","UIC","McClimon Track/Soccer Complex","Nonconference","—","Upcoming"),("2026-09-04","Michigan","U-M Soccer Stadium","Big Ten","D 1–1","Review"),("2026-09-10","Iowa","Home","Big Ten","W 2–0","Complete"),("2026-09-18","Minnesota","Away","Big Ten","L 0–1","Complete")]
    db.add_all([Match(id=i+1,date=d,opponent=o,venue=v,competition=c,result=r,status=s) for i,(d,o,v,c,r,s) in enumerate(matches)])
    players=[Player(id=i+1,team_id=1 if i<20 else 2,number=(i%20)+1,name=f"{'Wisconsin' if i<20 else 'Opponent'} Player {i%20+1}",role="Goalkeeper" if i%20==0 else "Outfield") for i in range(40)]; db.add_all(players)
    for i in range(20):
        sp=SetPiece(id=i+1,match_id=i%6+1,type="corner",attacking_team="Wisconsin" if i%3 else "Opponent",defending_team="Opponent",minute=8+i*3,video_end_time=5,notes="Synthetic demonstration data"); db.add(sp); db.add(Corner(id=i+1,side="left" if i%2 else "right",delivery=["inswing","outswing","driven"][i%3],delivery_zone=["near_post","central_six","far_post"][i%3],routine_family="screen and release",defensive_scheme="hybrid",first_contact_team="Wisconsin" if i%3 else "Opponent",shot=i%2==0,shot_xg=.12 if i%2==0 else 0,goal=i==4,possession_retained=i%3!=0,counterattack_conceded=i%7==0))
    for i in range(10):
        sid=21+i; db.add(SetPiece(id=sid,match_id=i%6+1,type="penalty",attacking_team="Wisconsin" if i<5 else "Opponent",defending_team="Opponent",minute=65+i,video_end_time=3,notes="Synthetic demonstration data")); db.add(Penalty(id=sid,penalty_context="shootout" if i>=5 else "regulation",shootout_round=i-4 if i>=5 else None,taker_id=2+i,goalkeeper_id=21,outcome="saved" if i in (3,7) else "goal",goal_x=[-2.5,2.1,0.2][i%3],goal_z=[.35,1.7,1.0][i%3],shot_direction=["left","right","center"][i%3],shot_height=["low","high","medium"][i%3],goalkeeper_dive_direction=["right","left","center"][i%3],estimated_speed=92+i,runup_length=4.2))
    db.add_all([Finding(match_id=1,title="First contact advantage",description="Wisconsin won first contact on 7 of 11 attacking corners.",confidence="moderate",sample_size=11),Finding(match_id=1,title="Opponent adjustment",description="The opponent changed marking structure after halftime.",confidence="exploratory",sample_size=6)])
    db.commit()
print("Seeded synthetic demo database")
