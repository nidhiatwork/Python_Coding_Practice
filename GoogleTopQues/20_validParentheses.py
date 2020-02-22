'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Input: "([)]"
Output: false
'''

def isValid(s):
    stack = []
    m = {')':'(',']':'[','}':'{'}
    for i in s:
        if i in m:
            if not stack or stack.pop() != m[i]:
                return False
        else:
            stack.append(i)
            
    return len(stack) == 0

def isValid_my(s):
    if not s:
        return True
    
    d = {'(':')','{':'}','[':']'}
    stack = []
    closing_braces = []
    for i in range(len(s)):
        if s[i] in d:
            #opening braces
            stack.append(s[i])
            closing_braces.append(d[s[i]])
        else:
            # closing braces
            if not closing_braces or s[i]!=closing_braces[-1]:
                return False
            stack.pop()
            closing_braces.pop()
    
    if not stack:
        return True
    return False


s = "()[]{}"
print(isValid(s))
