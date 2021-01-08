'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.
'''
import collections
def canConstruct(ransomNote, magazine):
    m = collections.Counter(magazine)
    for s in ransomNote:
        if s not in m or m[s]==0:
            return False
        m[s]-=1
    return True

ransomNote, magazine = "aa", "ab"
print(canConstruct(ransomNote, magazine))