'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''
import collections
def groupAnagrams_1(strs):
        ans = collections.defaultdict(list)
        for s in strs:
                ans[tuple(sorted(s))].append(s)
        return list(ans.values())

def groupAnagrams_2(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())

strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print(groupAnagrams_2(strs))