'''
Given an integer k, for every consecutive sequence of k days (calories[i], calories[i+1], ..., calories[i+k-1] for all 0 <= i <= n-k), they look at T, the total calories consumed during that sequence of k days (calories[i] + calories[i+1] + ... + calories[i+k-1]):

If T < lower, they performed poorly on their diet and lose 1 point; 
If T > upper, they performed well on their diet and gain 1 point;'''


def do(S,K):
    ws=0
    subs=0
    while ws<=len(S)-K:
        seen = set()
        for we in range(K):
            if S[ws+we] not in seen:
                seen.add(S[ws+we])
            else:
                break
        if len(seen)==K:
            subs+=1
        ws=ws+1
    return subs

print(do("havefunonleetcode", 5))
                          