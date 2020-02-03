'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
'''

def isIsomorphic(s,t):

    if len(s)!=len(t):
        return False
    
    m = dict()
    for i,c in enumerate(s):
        if c in m:
            if m[c]!=t[i]:
                return False
        else:
            if t[i] not in m.values():
                m[c]=t[i]
            else:
                return False
    return True

s="egg"
t="add"
print(isIsomorphic(s,t))