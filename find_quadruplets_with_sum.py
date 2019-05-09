



def find_quadruplets_with_sum(nums, target):
    if len(nums)<4:
        return []
    ans=[]
    nums.sort()
    print(nums)
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            k=j+1
            l=n-1
            while k<l:
                sum = nums[i] + nums[j] + nums[k] + nums[l]
                if sum==target:
                    data = [nums[i],nums[j],nums[k],nums[l]]
                    if data not in ans:
                        ans.append(sorted(data))
                if sum<target:
                    k+=1
                else:
                    l-=1
    ans = sorted(ans, reverse=True)
    return ans

print(find_quadruplets_with_sum([1, 0, -1, 0, -2, 2],0))