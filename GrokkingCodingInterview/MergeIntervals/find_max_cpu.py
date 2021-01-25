'''We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

Example 1:

Jobs: [[1,4,3], [2,5,4], [7,9,6]]
Output: 7
'''

from heapq import *
def find_max_cpu(jobs):
    jobs.sort(key=lambda x:x[0])
    minheap = []
    max_load = 0
    cur_load = 0
    heappush(minheap, (jobs[0][1],jobs[0][2]))
    for job in jobs[1:]:
        if len(minheap)>0 and minheap[0][0]<=job[0]:
            cur_load-=minheap[0][1]
            heappop(minheap)
        heappush(minheap,(job[1],job[2]))
        cur_load+=job[2]
        max_load=max(max_load,cur_load)
    return max_load


jobs = [[1,4,3], [2,5,4], [7,9,6]]
print(find_max_cpu(jobs))