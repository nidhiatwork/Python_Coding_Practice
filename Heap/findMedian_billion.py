from heapq import *


class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])

m = MedianFinder()
m.addNum(5)
m.addNum(2)
m.addNum(3)
m.addNum(7)
m.addNum(12)
m.addNum(6)
m.addNum(13)
m.addNum(9)
m.addNum(10)
m.addNum(3)
m.addNum(6)
m.addNum(3)
m.addNum(10)