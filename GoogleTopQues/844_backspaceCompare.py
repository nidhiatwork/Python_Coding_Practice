'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".'''

def backspaceCompare(S, T):
    st1,st2 = [],[]
    for c in S:
        if c!='#':
            st1.append(c)
        else:
            if st1:
                st1.pop()
    for c in T:
        if c!='#':
            st2.append(c)
        else:
            if st2:
                st2.pop()

    return "".join(st1) == "".join(st2)

S = "ab#c"
T = "ad#c"
print(backspaceCompare(S, T))

