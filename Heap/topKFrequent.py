'''Given a non-empty array of integers, return the key most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], key = 2
Output: [1,2]
'''
import collections
import heapq
from collections import defaultdict

def topKFrequent_1(nums, key):
    count = collections.Counter(nums)   
    return heapq.nlargest(key, count.keys(), key=count.get)

def topKFrequent_2(nums, k):
    hs = collections.Counter(nums)
    frq = defaultdict(list)
    for key,v in hs.items():
        frq[v].append(key)
    arr = []
    for x in range(len(nums), 0, -1):
        if x in frq:
            for i in frq[x]:
                if k:
                    arr.append(i)
                    k-=1
                else:
                    break
    return arr

print(topKFrequent_2([7,3,6,3,3,1,3,6],2))
