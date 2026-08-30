from app.services.spatial_analytics import distance, velocity, nearest_defender
from app.services.corner_analytics import CornerAnalyticsService
from app.services.penalty_analytics import PenaltyAnalyticsService
def test_spatial():
 assert distance((0,0,0),(3,4,0))==5; assert velocity((0,0,0),(2,4,0),0,2)==(1,2,0); assert nearest_defender((0,0,0),[(4,0,0),(1,0,0)])==(1,0,0)
def test_corner_metrics():
 x=CornerAnalyticsService.summarize([{"first_contact_team":"Wisconsin","shot":True,"goal":False,"shot_xg":.2,"possession_retained":True}]); assert x["shot_rate"]==1 and x["average_xg"]==.2
def test_penalty_shrinkage():
 x=PenaltyAnalyticsService.get_smoothed_conversion_rate(1,1); assert x["posterior_mean"]<1 and x["sample_size"]==1
