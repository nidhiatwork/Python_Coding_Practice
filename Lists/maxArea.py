'''
11. Container With Most Water
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''
import sys
def maxArea_bruteForce(height):
    i=1
    max_area = -sys.maxsize
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            area = (j-i)*min(height[i], height[j])
            if area > max_area:
                max_area = area
    return max_area

def maxArea_optimal(height):
    maxarea = 0
    l = 0
    r = len(height) - 1
    while (l < r):
        maxarea = max(maxarea, min(height[l], height[r]) * (r - l))
        if (height[l] < height[r]):
            l+=1
        else:
            r-=1

    return maxarea

height = [1,8,6,2,5,4,8,3,7] 
print(maxArea_optimal(height))