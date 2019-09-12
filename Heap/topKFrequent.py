'''Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
'''
import collections
import heapq
from collections import defaultdict

def topKFrequent_1(nums, k):
    count = collections.Counter(nums)   
    return heapq.nlargest(k, count.keys(), key=count.get)

def topKFrequent_2(nums, k):
    frq = defaultdict(list)
    c = collections.Counter(nums)
    for key, cnt in c.items():
        frq[cnt].append(key)

    res = []
    for times in reversed(range(len(nums) + 1)):
        res.extend(frq[times])
        if len(res) >= k: 
            return res[:k]
    return res[:k]


print(topKFrequent_2([7,3,6,3,3,1,3,6],2))
