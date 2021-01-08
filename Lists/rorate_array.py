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
            k=0
        ans.append(a[k])
        k=k+1
    return ans

def rotate_inPlace(a,k):
    k=k%len(a)
    while k:
        val = a[0]
        j = 0
        while j< len(a)-1:
            a[j]=a[j+1]
            j+=1
        a[j]=val
        k-=1
    return a

a = [3,6,8,3,2,6]
k=8
print(rotate(a,k))
print(rotate_inPlace(a,k))