from math import acos, hypot, sqrt

def distance(a,b): return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)
def velocity(p1,p2,t1,t2): return tuple((b-a)/(t2-t1) for a,b in zip(p1,p2))
def acceleration(v1,v2,t1,t2): return tuple((b-a)/(t2-t1) for a,b in zip(v1,v2))
def run_vector(p1,p2): return tuple(b-a for a,b in zip(p1,p2))
def angle_between_players(origin,a,b):
    u=(a[0]-origin[0],a[1]-origin[1]); v=(b[0]-origin[0],b[1]-origin[1]); return acos(max(-1,min(1,(u[0]*v[0]+u[1]*v[1])/(hypot(*u)*hypot(*v)))))
def distance_to_goal(p,goal=(105,34,0)): return distance(p,goal)
def nearest_defender(attacker, defenders): return min(defenders,key=lambda d: distance(attacker,d))
def attacker_defender_separation(attacker, defenders): return distance(attacker,nearest_defender(attacker,defenders))
def player_density(center,players,radius=10): return sum(distance(center,p)<=radius for p in players)/(3.14159*radius**2)
