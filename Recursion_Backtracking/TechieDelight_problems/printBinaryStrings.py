from collections import deque

def printBinaryPattern_recursion(s,ss='',i=0):
    if i==len(s):
        print(ss)
        
    else:
        if s[i]=='?':
            for c in "01":
                printBinaryPattern_recursion(s,ss+c,i+1)  
        else:
            printBinaryPattern_recursion(s,ss+s[i],i+1)      

s = "1?11?00?1?"
printBinaryPattern_recursion(s)



# Find all binary strings that can be formed from given
# wildcard pattern
def printBinaryPattern_iterative(pattern):

	# create an empty stack (we can also use set, deque
	# or any other container)
	stack = deque()
	stack.append(pattern)  # push the pattern into the stack

	# loop till stack is empty
	while stack:

		# pop string from stack and process it
		curr = stack.pop()

		# index stores position of first occurrence of wildcard
		# pattern in curr
		index = curr.find('?')
		if index != -1:
			# replace '?' with 0 and 1 and push it to the stack
			for ch in "01":
				curr = curr[:index] + ch + curr[index + 1:]
				stack.append(curr)

		# If no wildcard pattern is found, print the string
		else:
			print(curr)

s = "1?0?"
printBinaryPattern_iterative(s)
