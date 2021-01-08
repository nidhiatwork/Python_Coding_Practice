'''
Reshape the matrix
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
'''
from collections import deque
def matrixReshape(nums,r,c):
  if not nums or len(nums)*len(nums[0])!=r*c:
        return nums
  ans = [[]]
  for i in range(len(nums)):
      for j in range(len(nums[0])):
          k = nums[i][j]
          if len(ans[-1]) < c:
              ans[-1].append(k)
          else:
              ans.append([k])
  return ans


nums = [[1,2,4],
 [3,4,9]]
r,c = 3,2
print(matrixReshape(nums,r,c)) 