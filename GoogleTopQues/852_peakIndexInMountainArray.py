'''

'''

def peakIndexInMountainArray(A):
    if len(A)<3:
        return -1
    i,j,n=0,len(A)-1,len(A)
    while i+1<n and A[i+1]>A[i]:
        i+=1
    while j>0 and A[j]<A[j-1]:
        j-=1
    
    return i if i==j and i>0 and j<n-1 else -1

A = [0,1,0]
print(peakIndexInMountainArray(A))
