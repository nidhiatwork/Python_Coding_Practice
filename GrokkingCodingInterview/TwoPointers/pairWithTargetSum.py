def pairWithTargetSum(arr, target):
    left,right=0,len(arr)-1
    ans = []
    while left<right:
        sum=arr[left]+arr[right]
        if sum>target:
            right-=1
        elif sum<target:
            left+=1
        else:
            ans.append(left)
            ans.append(right)
    return ans