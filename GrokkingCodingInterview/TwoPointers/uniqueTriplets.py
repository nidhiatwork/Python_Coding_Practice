'''
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
'''
def do(arr):
    triplets=[]
    arr.sort()
    for f in range(len(arr)-1):
        s,t = f+1,len(arr)-1
        while s<t:
            sum = arr[f]+arr[s]+arr[t]
            if sum==0:
                triplets.append([arr[f],arr[s],arr[t]])
                s+=1
                t-=1
                while s<t and arr[s]==arr[s-1]:
                    s+=1
                while s<t and arr[t]==arr[t==1]:
                    t-=1
            elif sum<0:
                s+=1
            else:
                t-=1
    return triplets

print(do([-3, 0, 1, 2, -1, 1, -2]))

