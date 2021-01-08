
'''Reverse a string in place using O(1)'''

def reverse_string(s):
    l = len(s)
    if l < 2:
        return s
    return reverse_string_sub(s[l//2:]) + reverse_string_sub(s[:l//2])

def reverse_string_sub(s):
    i,j=0,len(s)-1
    while i<j:
        s[i],s[j]=s[j],s[i]
        i,j=i+1,j-1
    return s


def reverseString_usingNegate(s):
    s = list(s)
    for i in range(len(s) // 2):
        s[i], s[~i] = s[~i], s[i]
    return s


s = ["H","a","n","n","a","h"]
print(reverseString_usingNegate(s))