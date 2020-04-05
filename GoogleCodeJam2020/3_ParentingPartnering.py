
T = int(input())
t=1
while t<=T:
    n_activity = int(input())
    activities = []
    for i in range(n_activity):
        a = input().strip().split(" ")
        a.append(i)
        activities.append([int(x) for x in a])
    result = [None]*len(activities)
    activities.sort(key=lambda x:x[0])
    d = {'J':0,'C':0}
    for activity in activities:
        if activity[0]>=d['C']:
            result[activity[2]]='C'
            d['C']=activity[1]
        elif activity[0]>=d['J']:
            result[activity[2]]='J'
            d['J']=activity[1]
        else:
            result="IMPOSSIBLE"
            break
    ans = "Case #"+str(t)+": "+''.join(result)
    print(ans)
    t+=1
