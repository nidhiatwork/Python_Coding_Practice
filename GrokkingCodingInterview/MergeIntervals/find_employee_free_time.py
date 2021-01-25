'''For ‘K’ employees, we are given a list of intervals representing the working hours of each employee. Our goal is to find out if there is a free interval that is common 
to all employees. You can assume that each list of employee working hours is sorted on the start time.

Example 1:

Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]]
Output: [3,5]
Explanation: Both the employess are free between [3,5].
'''

from heapq import *
# class Interval:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
    
#     def print_interval(self):
#         print("[",str(self.start),", ",str(self.end),"]")


class EmployeeInterval:
    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval
        self.employeeIndex = employeeIndex
        self.intervalIndex = intervalIndex

    def __lt__(self, other):
        return self.interval.start<other.interval.start


def find_employee_free_time(schedule):
    if not schedule:
        return []

    n = len(schedule)
    result, minHeap = [], []
    for i in range(n):
        heappush(minHeap, EmployeeInterval(schedule[i][0], i, 0))
    
    previousInterval = minHeap[0].interval   #interval with smallest start time
    while minHeap:
        queueTop = heappop(minHeap)
        if previousInterval.end < queueTop.interval.start:
            result.append(Interval(previousInterval.end, queueTop.interval.start))
            previousInterval = queueTop.interval
        else:
            if previousInterval.end < queueTop.interval.end:
                previousInterval = queueTop.interval
        
        employeeSchedule = schedule[queueTop.employeeIndex]
        if len(employeeSchedule)>queueTop.intervalIndex+1:
            heappush(minHeap,EmployeeInterval(employeeSchedule[queueTop.intervalIndex+1], queueTop.employeeIndex, queueTop.intervalIndex+1))
    return result

# schedule = [[Interval(1,3), Interval(9,12)], [Interval(2,4),Interval(6,8)]]
# intervals = find_employee_free_time(schedule)
# for interval in intervals:
#     interval.print_interval()


'''
If some interval overlaps any interval (for any employee), then it won't be included in the answer. So we could reduce our problem to the following: given a set of intervals, find all places where there are no intervals.

To do this, we can use an "events" approach present in other interval problems. For each interval [s, e], we can think of this as two events: balance++ when time = s, and balance-- when time = e. We want to know the regions where balance == 0.
'''
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
    def print_interval(self):
        print("[",str(self.start),", ",str(self.end),"]")

def employeeFreeTime(avails):
    OPEN, CLOSE = 0, 1

    events = []
    for emp in avails:
        for interval in emp:
            events.append((interval.start, OPEN))
            events.append((interval.end, CLOSE))

    events.sort()
    ans = []
    prev = None
    bal = 0
    for cur, cmd in events:
        if bal == 0 and prev is not None:
            ans.append(Interval(prev, cur))

        bal += 1 if cmd is OPEN else -1
        prev = cur

    return ans

schedule = [[Interval(1,3), Interval(9,12)], [Interval(2,4),Interval(6,8)]]
intervals = employeeFreeTime(schedule)
for interval in intervals:
    interval.print_interval()