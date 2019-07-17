'''
Given an encoded string in form of : 'ab[cd]{2}def'
You have to return decoded string : 'abcdcddef".
'''
from collections import deque
def decodestring_easy(mystr):
    i = 0
    stack = []
    while i < len(mystr):
	    c = mystr[i]
	    if c== '[':
		    stack.append(c)
	    elif c == ']':
		    temp = ""
		    while(stack[len(stack)-1]!='['):
			    temp = stack.pop() + temp
		    stack.pop()
		    stack.append(temp)
	    elif c == '{':
		    num = 0
		    i += 1
		    while i<len(mystr) and mystr[i] != '}':
			    num = num*10 + int(mystr[i])
			    i += 1
		    pre = stack.pop()
		    temp = ""
		    while num!=0:
		    	temp = temp + pre
		    	num -= 1
		    stack.append(temp)
			# print(temp)
	    else: 
		    stack.append(c)
	    i += 1
    res_str = ""
    while len(stack)!=0:
	    res_str = stack.pop() + res_str

    return res_str

def decodestring_withAuthenticity(decoder):
    ans = ''
    dq = deque()
    traceback = False
    for i in range(len(decoder)):
        if decoder[i] != '}':
            dq.append(decoder[i])
            continue
        else:
            traceback = True
            num = ''
            while traceback:
                if len(dq) <= 0: 
                    return 'string not valid, stack has emptied' ## safety check that dq doesn't empty out
                ch = dq.pop()
                if ch != '{':
                    num = ch + num
                else:
                    traceback = False
            if dq.pop() != ']': ## validate that there is a closing bracket at the top of the stack
                return 'closing bracket not found'
            traceback = True
            s = ''
            while traceback:
                if len(dq) <= 0: 
                    return 'string not valid, stack has emptied' ## safety check that dq doesn't empty out
                ch = dq.pop()
                if ch == '[':
                    traceback = False
                    continue
                elif ch.isalpha():
                    s = ch + s
                else:
                    continue
            s = s*int(num)
            for j in range(len(s)):
                dq.append(s[j])
    while len(dq):
        ans += dq.popleft()
    return ans



s = "def[ab[cd]{2}]{3}ghi"
print(decodestring_easy(s))
print(decodestring_withAuthenticity(s))