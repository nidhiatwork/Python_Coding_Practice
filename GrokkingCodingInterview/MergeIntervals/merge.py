'''Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.'''

from collections import Counter
def merge(intervals):
    merged = []
    intervals.sort(key=lambda interval: interval[0])
    start = intervals[0][0]
    end = intervals[0][-1]
    for i in range(1, len(intervals)):
        cur_start = intervals[i][0]
        cur_end = intervals[i][-1]
        if cur_start<=end:
            end = max(end,cur_end)
        else:
            merged.append([start, end])
            start = cur_start
            end = cur_end
    merged.append([start, end])
    return merged

intervals = [[6,7], [2,4], [5,9]]
print(merge(intervals))