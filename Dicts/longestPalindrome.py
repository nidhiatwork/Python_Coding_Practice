'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.
Note:
Assume the length of given string will not exceed 1,010.
Input:
"abccccdd"
Output:
7
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''
from collections import Counter
def longestPalindrome_1(s):
    d = Counter(s)
    sorted_items = sorted(d.items(), key = lambda x: x[1], reverse=True)
    odd = False
    for k,v in sorted_items:
        if v%2:
            if not odd:
                odd = True
            else:
                sorted_items.remove((k,v))
        
    print(sorted_items)
    return sum([v for k,v in sorted_items])

def longestPalindrome_2(s):
        ans = 0
        vals = Counter(s).values()
        oddFound = False
        for v in vals:
            ans += v // 2 * 2
            if v % 2 == 1 and not oddFound:
                ans += 1
                oddFound = True
        return ans


s = 'abccccdd'
print(longestPalindrome_1(s))
print(longestPalindrome_2(s))