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


s = "([(({}))])[({})]{[]}"
print(isValid(s))
