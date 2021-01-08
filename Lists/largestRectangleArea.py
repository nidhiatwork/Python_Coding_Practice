'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
'''

def largestRectangleArea(heights):
    res = 0
    for i in range(len(heights)):
        if (i + 1 < len(heights) and heights[i] <= heights[i+1]): 
            continue 
        minh = heights[i]
        for j in range(i,-1,-1):
            minh = min(minh, heights[j])
            res = max(res, minh * (i - j + 1))
    return res

print(largestRectangleArea([2,1,5,6,2,3]))
