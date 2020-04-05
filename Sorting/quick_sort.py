def partition(nums,low,high): 
    pivot_index = (low+high)//2
    nums[pivot_index],nums[high] = nums[high], nums[pivot_index]
    i=low
    for j in range(low, high): 
        if   nums[j] <= nums[high]: 
            print("Swapping: ", nums[i],nums[j])
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
    
    print("Final swap: ",nums[i],nums[high])  
    nums[i],nums[high] = nums[high],nums[i] 
    print(nums)
    return i
  
def quick_sort(nums,low,high): 
    if low < high: 
        pivot_index = partition(nums,low,high) 
        quick_sort(nums, low, pivot_index-1) 
        quick_sort(nums, pivot_index+1, high) 
  
nums = [10, 3, 8, 9, 1, 5]
n = len(nums)
quick_sort(nums,0,n-1) 
print(nums) 
