'''
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
'''
import math
import sys
import heapq

def kClosest(points, K):
    heap = []
    
    for (x, y) in points:
        dist = -(x*x + y*y)
        if len(heap) == K:
            heapq.heappushpop(heap, (dist, x, y))
        else:
            heapq.heappush(heap, (dist, x, y))
    
    return [(x,y) for (dist,x, y) in heap]


def kClosest_1(points, K):
    points.sort(key = lambda x: x[0]**2 + x[1]**2)
    return points[:K]

points = [[3,3],[5,-1],[-2,4],[2,3],[1,6],[-2,5]]
K = 2
print(kClosest_1(points, K))