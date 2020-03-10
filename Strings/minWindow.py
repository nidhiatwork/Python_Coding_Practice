'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''
#To do
import sys
import collections

def minWindow_mySolution(s,t):
    l,r=0,0
    minm = sys.maxsize
    window = ""
    while r<len(s):
        print(s[l:r+1])
        if not occurrence(s[l:r+1],t):
            r+=1
        else:
            while(occurrence(s[l:r+1],t)):
                if len(s[l:r+1])<minm:
                    minm = len(s[l:r+1])
                    window = s[l:r+1]
                l+=1
    return window

def occurrence(ss,tt):
    d = collections.Counter(ss)
    for c in tt:
        if c not in d or d[c]==0:
            return False
        d[c]-=1
    return True

def minWindow_2(s, t):
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]


def minWindow(s, t):
    need = collections.Counter(t)            #hash table to store char frequency
    missing = len(t)                         #total number of chars we care
    start, end = 0, 0
    i = 0
    for j, char in enumerate(s, 1):          #index j from 1
        if need[char] > 0:
            missing -= 1
        need[char] -= 1
        if missing == 0:                     #match all chars
            while i < j and need[s[i]] < 0:  #remove chars to find the real start
                need[s[i]] += 1
                i += 1
            need[s[i]] += 1                #ensure the first appearing char satisfies need[char]>0
            missing += 1                   #we missed this first char, so add missing by 1
            if end == 0 or j-i < end-start:  #update window
                start, end = i, j
            i += 1                         #update i to start+1 for next window
    return s[start:end]

# s="cabwefgewcwaefgcf"
# t="cae"
s="ADOBECODEBANC"
t="ABC"
print(minWindow(s,t))