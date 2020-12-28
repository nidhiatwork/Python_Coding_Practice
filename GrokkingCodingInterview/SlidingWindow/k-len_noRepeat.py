
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
                          