'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''
def isPalindrome_1(s):
    str = ""
    for c in s:
        if c.isalnum():
            str +=c.lower()
    l,h=0,len(str)-1
    while l < h:
        if str[l]!=str[h]:
            return False
        l+=1
        h-=1
    return True

def isPalindrome_2(s):
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        else:
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome_2(s))