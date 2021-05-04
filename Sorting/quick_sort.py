
  
def partition_lastElement(nums,low,high): 
    i = low
    for j in range(low,high):
        if nums[j]<=nums[high]:
            nums[i],nums[j] = nums[j], nums[i]
            i+=1
    nums[i],nums[high]=nums[high],nums[i]
    print(nums)
    return i

def partition_midElement(nums,low,high): 
    pivot_index = (low+high)//2
    nums[pivot_index],nums[high] = nums[high], nums[pivot_index]
    i=low
    for j in range(low, high): 
        if   nums[j] <= nums[high]: 
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
    nums[i],nums[high] = nums[high],nums[i] 
    print(nums)
    return i

def quick_sort(nums,low,high): 
    if low < high: 
        pivot_index = partition_lastElement(nums,low,high)
        print("pivot: ",nums[pivot_index])
        quick_sort(nums, low, pivot_index-1) 
        quick_sort(nums, pivot_index+1, high) 
  
nums = [4,2,5,12,71,34,13,9,54,23,45,64,34]
n = len(nums)
quick_sort(nums,0,n-1) 
