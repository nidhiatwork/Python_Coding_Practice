'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
'''
def do(s):
    low,high = 0,len(s)-1
    s = list(s)
    while low<high:
        while low<len(s) and s[low] not in 'aeiouAEIOU':
            low+=1
        while high>=0 and s[high] not in 'aeiouAEIOU':
            high-=1
        if low>=high:
            return ''.join(s)
        s[low],s[high]=s[high],s[low]
        low+=1
        high-=1
    return ''.join(s)

print(do(".,"))