"""
a = [2,3,1,7]
k = 2
[1,7,2,3]
"""

def rotate(a,k):
    ans = []
    k=k%len(a)
    for i in range(len(a)):
        if k==len(a):
            k=len(a)-k
        ans.append(a[k])
        k=k+1
    return ans

print(rotate([2,3,1,7],5))