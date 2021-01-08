'''
Given a string, find the first non-repeating character in it and return it'input_str index. If it doesn't exist, return -1.

Examples:

input_str = "leetcode"
return 0.

input_str = "loveleetcode",
return 2.
'''
import collections
def firstUniqChar_1(input_str):
    counts = collections.Counter(input_str)
    for k,v in counts.items():
          if v==1:
                return input_str.find(k)
    return -1

def firstUniqChar_2(input_str):
    s = set(input_str)
    idxs = []
    for c in s:
          if input_str.count(c)==1:
                idxs.append(input_str.find(c))
    if not idxs:
          return -1
    return min(idxs)

input_str = "aass"
print(firstUniqChar_2(input_str))  
