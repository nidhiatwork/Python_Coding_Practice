'''
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    '''

def titleToNumber(s):
    ans = 0
    for i,c in enumerate(reversed(s)):
        ans +=(ord(c)-64)*(26**i)
    return ans
    # return sum([ (ord(c)-64)*(26**i) for i,c in enumerate(reversed(s))])

s = 'AB'
print(titleToNumber(s))
