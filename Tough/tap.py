'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''
def tap(height):
  res = 0
  n = len(height)
  if not n: 
    return res
  ltr,rtl = [None]*n,[None]*n
  ltr[0] = height[0]
  rtl[n-1] = height[-1]
  for i in range(1,n):
      ltr[i] = max(ltr[i-1], height[i])
  for i in range(n-2,-1,-1):
      rtl[i] = max(rtl[i+1], height[i])
  for i in range(n):
      res += min(ltr[i], rtl[i]) - height[i]
  return res

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(tap(height))