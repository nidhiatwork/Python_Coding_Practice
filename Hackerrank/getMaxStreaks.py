def getMaxStreaks(toss):
    return [f(toss,'H'), f(toss,'T')]

def f(toss, c):
    ct=0
    mx_ct=0
    for i in range(len(toss)):
        if toss[i]!=c:
            mx_ct=max(mx_ct,ct)
            ct=0
        else:
             ct+=1
    return max(mx_ct,ct)   

            




toss = ['T','H', 'H', 'T', 'H', 'T', 'T','T']
print(getMaxStreaks(toss))