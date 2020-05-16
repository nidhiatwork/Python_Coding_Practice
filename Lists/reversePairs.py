'''
Given an array nums, we call (i, j): an important reverse pair if i < j and nums[i] > 2*nums[j].
You need to return the number of important reverse pairs in the given array.

Input: [1,3,2,3,1]
Output: 2

Input: [2,4,3,5,1]
Output: 3
'''


def reversePairs_1(nums):
    # exponential complexity
    count = 0
    d= dict()
    for i in range(len(nums)):
        d[i] = nums[i]
    d=sorted(d.items(), key= lambda p: p[1], reverse=True)
    i,j=0,len(d)-1
    while i<len(d):
        if d[i][1]>2*d[j][1]:
            if d[i][0]<d[j][0]:
                count+=1
            j-=1
            
        else:
            i+=1
            j=len(d)-1
        if j==i:
            if i!=0:
                i+=1
                j=len(d)-1
            else:
                break
    return count

def reversePairs_2(nums):
    return sum([nums[j]>2*nums[i] for i in range(len(nums)) for j in range(0, i)])

def merge(A, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid
    L,R = list(),list()
    for i in range(n1):
        L[i] = A[start + i]
    for j in range(n2):
        R[j] = A[mid + 1 + j]
    i,j = 0,0
    for k in range(start,end+1): 
        if (j >= n2 or (i < n1 and L[i] <= R[j])):
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1
    

def mergesort_and_count(A,  start,  end):

    if (start < end): 
        mid = (start + end) // 2
        count = mergesort_and_count(A, start, mid) + mergesort_and_count(A, mid + 1, end)
        j = mid + 1
        for i in range(start,mid+1): 
            while (j <= end and A[i] > A[j] * 2):
                j+=1
            count += j - (mid + 1)
        
        merge(A, start, mid, end)
        return count
    
    else:
        return 0


def reversePairs_3(nums):
    return mergesort_and_count(nums, 0, len(nums)- 1)



nums = [-5,-5]
 #[2,4,3,5,1] # (1, 3):, (3, 3):, (2, 2):, (0, 1):, (4, 1):
print(reversePairs_1(nums))