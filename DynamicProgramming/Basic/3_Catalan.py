'''
Catalan numbers are a sequence of natural numbers that occurs in many interesting counting problems like following.
1) Count the number of expressions containing n pairs of parentheses which are correctly matched. For n = 3, possible expressions are 
((())), ()(()), ()()(), (())(), (()()).

2) Count the number of possible Binary Search Trees with n keys (See this)

3) Count the number of full binary trees (A rooted binary tree is full if every vertex has either two children or no children) with n+1 leaves.

The first few Catalan numbers for n = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …
Basic formula is: res += catalan(i) * catalan(n-i-1), 
where catalan(0)=1 & catalan(1) = 1

'''

# A recursive function to find nth catalan number 
def catalan(n): 
	# Base Case 
	if n <=1 : 
		return 1

	# Catalan(n) is the sum of catalan(i)*catalan(n-i-1) 
	res = 0
	for i in range(n): 
		res += catalan(i) * catalan(n-i-1)
	return res 

# Driver Program to test above function 
# print(catalan(5))

# A dynamic programming based function to find nth 
# Catalan number 
def dp_catalan(n): 
	if (n == 0 or n == 1): 
		return 1

	# Table to store results of subproblems 
	catalan = [0 for i in range(n + 1)] 

	# Initialize first two values in table 
	catalan[0] = 1
	catalan[1] = 1

	# Fill entries in catalan[] using recursive formula 
	for i in range(2, n + 1): 
		catalan[i] = 0
		for j in range(i): 
			catalan[i] = catalan[i] + catalan[j] * catalan[i-j-1] 

	# Return last entry 
	return catalan[n] 

# Driver code 
for i in range (10): 
	print (dp_catalan(i),end=" ") 
