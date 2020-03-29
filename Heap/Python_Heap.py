from heapq import heapify, heappop, heappush

heap = []
nums = [12,3,-2,6,4,8,9]

#If you need sorted order of array, use heappush followed by heappop

# Create heap by pushing elements one by one
for num in nums:
    heappush(heap, num)

# #Get min element one by one by popping
while heap:
    print(heappop(heap))

# Use heapify to save heap in form of array. Does not sort !!
heapify(nums)
print(nums)