'''
Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.
Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
'''
def do(arr,target):
    quadruplets=[]
    arr.sort()
    for f in range(len(arr)-3):
        for s in range(f+1,len(arr)-2):
            l,r = s+1,len(arr)-1
            while l<r:
                sum = arr[f]+arr[s]+arr[l]+arr[r]
                if sum==target:
                    quadruplets.append([arr[f],arr[s],arr[l],arr[r]])
                    l+=1
                    r-=1
                    while l<r and arr[l]==arr[l-1]:
                        l+=1
                    while l<r and arr[r]==arr[r+1]:
                        r-=1
                elif sum<target:
                    l+=1
                else:
                    r-=1
    return quadruplets

print(do([4, 1, 2, -1, 1, -3],1))

