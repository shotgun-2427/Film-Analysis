class CornerAnalyticsService:
    @staticmethod
    def summarize(rows):
        n=len(rows); rate=lambda key: sum(bool(r.get(key)) for r in rows)/n if n else 0
        return {"corners":n,"first_contact_rate":sum(r.get("first_contact_team")=="Wisconsin" for r in rows)/n if n else 0,"shot_rate":rate("shot"),"goal_rate":rate("goal"),"average_xg":sum(r.get("shot_xg",0) for r in rows)/n if n else 0,"second_ball_retention_rate":rate("possession_retained"),"counterattack_conceded_rate":rate("counterattack_conceded")}
