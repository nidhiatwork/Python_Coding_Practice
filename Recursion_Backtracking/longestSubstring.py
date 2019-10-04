'''
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
'''
from collections import Counter
def longestSubstring(s,k):
    print("Running for s:{} and k:{}".format(s,k))
    if len(s) < k:
        return 0
    c = min(set(s), key=s.count)
    print("Found c as: ",c)
    if s.count(c) >= k:
        return len(s)
    return max(longestSubstring(t, k) for t in s.split(c))


print(longestSubstring("ababacb",3))