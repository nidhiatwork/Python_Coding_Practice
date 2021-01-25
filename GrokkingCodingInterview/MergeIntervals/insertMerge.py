'''Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.'''

from collections import Counter
def insertMerge(intervals, new_interval):
    i=0
    merged = []
    while i<len(intervals) and intervals[i][-1]<new_interval[0]:
        merged.append(intervals[i])
        i+=1
    
    while i<len(intervals) and new_interval[-1]>=intervals[i][0]:
        new_interval[i][0] = min(new_interval[i][0], intervals[i][0])
        new_interval[i][-1] = max(new_interval[i][-1], intervals[i][-1])
        i+=1
    
    merged.append(new_interval)

    while i<len(intervals):
        merged.append(intervals[i])
        i+=1
    return merged
    
intervals = [[1,3], [5,7], [8,12]]
new_interval=[4,6]
print(insertMerge(intervals, new_interval))