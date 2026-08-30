from statistics import NormalDist
class PenaltyAnalyticsService:
    @staticmethod
    def get_smoothed_conversion_rate(goals, attempts, alpha=2, beta=2):
        a,b=alpha+goals,beta+attempts-goals; mean=a/(a+b); sd=(a*b/((a+b)**2*(a+b+1)))**.5; z=NormalDist().inv_cdf(.975)
        return {"posterior_mean":mean,"lower_interval":max(0,mean-z*sd),"upper_interval":min(1,mean+z*sd),"sample_size":attempts}
