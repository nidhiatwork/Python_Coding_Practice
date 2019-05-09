

def get_sum(nums, target):
        nums.sort()
        dic = {}
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:  #CAN SKIP THIS
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum < target:
                    l += 1
                    dic[sum] = target - sum
                elif sum > target:
                    r -= 1
                    dic[sum] = sum - target
                else:
                    return target
        return min(dic, key=dic.get)
        
arr = [-1,2,1,-4]
print(get_sum(arr,1))
# 0, 1, 1, 1