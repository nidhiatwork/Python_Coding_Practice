'''
Given an encoded string, return its decoded string.

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''

def decode_1(s):
    stack = []
    stack.append(["", 1])
    num = ""
    for ch in s:
        if ch.isdigit():
            num += ch
        elif ch == '[':
            stack.append(["", int(num)])
            num = ""
        elif ch == ']':
            c, n = stack.pop()
            stack[-1][0] += c*n
        else:
            stack[-1][0] += ch
        print(stack)
    return stack[0][0]

s = "3[a2[c]]"
print(decode_1(s))

