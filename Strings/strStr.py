'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''

def strStr_1(haystack, needle):
    if needle == "":
        return 0
    l = len(needle)
    if len(haystack)<l:
        return -1
    i=0
    while i<len(haystack):
        if haystack[i:i+l] == needle:
            return i
        i=i+1
    return -1

def strStr_2(haystack, needle):
    for i in range(len(haystack) - len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

haystack = "hello"
needle = "ll"
print(strStr_1(haystack, needle))