'''Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

'''

from collections import Counter
def intersection(intervals_a,intervals_b):
    i,j=0,0
    intersection_intervals = []
    while i < len(intervals_a) and j < len(intervals_b):
        if intersect(intervals_a[i],intervals_b[j]) or intersect(intervals_b[j],intervals_a[i]):
            interval = [max(intervals_a[i][0],intervals_b[j][0]), min(intervals_a[i][-1], intervals_b[j][-1])]
            intersection_intervals.append(interval)

        if intervals_a[i][-1]<intervals_b[j][-1]:
            i+=1
        else:
            j+=1
    return intersection_intervals

def intersect(a,b):
    return a[0]>=b[0] and a[0]<=b[-1]

intervals_a=[[1, 3], [5, 6], [7, 9]]
intervals_b=[[2, 3], [5, 7]]
print(intersection(intervals_a,intervals_b))