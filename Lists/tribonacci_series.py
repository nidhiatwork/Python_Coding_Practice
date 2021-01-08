
def tribonacci(n):
    t=dict()
    t[0]=0
    t[1]=1
    t[2]=1
    if n<=2:
        return t[n]
    i=3
    while i<=n:
        t[i] = t[i-3] + t[i-2] + t[i-1]
        i+=1
    return t[n]

n = 37
print(tribonacci(n))