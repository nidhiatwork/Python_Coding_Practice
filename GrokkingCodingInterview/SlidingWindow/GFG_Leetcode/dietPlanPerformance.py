'''
Given an integer k, for every consecutive sequence of k days (calories[i], calories[i+1], ..., calories[i+k-1] for all 0 <= i <= n-k), they look at T, the total calories consumed during that sequence of k days (calories[i] + calories[i+1] + ... + calories[i+k-1]):

If T < lower, they performed poorly on their diet and lose 1 point; 
If T > upper, they performed well on their diet and gain 1 point;'''


def dietPlanPerformance(calories, k,lower, upper):
    points = 0
    ws=0
    sm=0
    for we in range(len(calories)):
        sm+=calories[we]
        if we-ws+1==k:
            if sm<lower:
                points-=1
            if sm>upper:
                points+=1
            sm-=calories[ws]
            ws+=1
    return points