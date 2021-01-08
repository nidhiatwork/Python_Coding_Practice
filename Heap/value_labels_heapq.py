import collections 
import heapq

def largestValsFromLabels(values, labels, num_wanted, use_limit):
    queue = [(-value, label) for value, label in zip(values, labels)]
    heapq.heapify(queue)
    counter = collections.Counter()
    res = 0
    count = 0
    while queue:
        neg_value, label = heapq.heappop(queue)
        if count < num_wanted and counter[label] < use_limit:
            counter[label] += 1
            res += -neg_value
            count += 1
    return res



values = [5,4,3,2,1]
labels = [1,3,3,3,2]
num_wanted = 3
use_limit = 2

print(largestValsFromLabels(values,labels,num_wanted,use_limit))