'''
Given two strings s and t , write a function to determine if t is an anagram of s.
'''
from collections import Counter

def isAnagram_using2Counters(s,t):
    if len(t)!=len(s):
        return False
    s_counter = Counter(s)
    t_counter = Counter(t)
    for k,v in s_counter.items():
        while v:
            if k not in t_counter or t_counter[k]==0:
                return False
            t_counter[k]-=1
            v-=1
    return True

def isAnagram_using1CharDict(s,t):
    if len(t)!=len(s):
        return False
    counter = dict()
    for i in range(len(s)):
        print("Adding "+s[i]+" count by 1")
        counter[s[i]] = counter.get(s[i],0)+1
        print("Decreasing "+t[i]+" count by 1")
        counter[t[i]] = counter.get(t[i],0)-1

    for count in counter.values():
        if (count != 0):
            return False
    return True

s,t='anagram','naagmra'
print(isAnagram_using1CharDict(s,t))