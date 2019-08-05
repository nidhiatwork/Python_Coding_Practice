import heapq
def findKthLargest1(nums, k):
    return sorted(nums, reverse=True)[k-1]
    
# O(nk) time, bubble sort idea, TLE
def findKthLargest2(nums, k):
    for i in range(k):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                # exchange elements, time consuming
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums[len(nums)-k]
    
# O(nk) time, selection sort idea
def findKthLargest3(nums, k):
    for i in range(len(nums), len(nums)-k, -1):
        tmp = 0
        for j in range(i):
            if nums[j] > nums[tmp]:
                tmp = j
        nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
    return nums[len(nums)-k]
    
# O(k+(n-k)lgk) time, min-heap
def findKthLargest4(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    for _ in range(len(nums)-k):
        heapq.heappop(heap)
    return heapq.heappop(heap)

# O(k+(n-k)lgk) time, min-heap        
def findKthLargest5(nums, k):
    return heapq.nlargest(k, nums)[k-1]
    
# O(n) time, quick selection
def findKthLargest(nums, k):
    # convert the kth largest to smallest
    return findKthSmallest(nums, len(nums)+1-k)
    
def findKthSmallest(nums, k):
    if nums:
        pos = partition(nums, 0, len(nums)-1)
        if k > pos+1:
            return findKthSmallest(nums[pos+1:], k-pos-1)
        elif k < pos+1:
            return findKthSmallest(nums[:pos], k)
        else:
            return nums[pos]
 
# choose the right-most element as pivot   
def partition(nums, l, r):
    low = l
    while l < r:
        if nums[l] < nums[r]:
            nums[l], nums[low] = nums[low], nums[l]
            low += 1
        l += 1
    nums[low], nums[r] = nums[r], nums[low]
    return low

nums = [5,2,1,7,7,4,2,4]
k = 2
print(findKthLargest1(nums,k))