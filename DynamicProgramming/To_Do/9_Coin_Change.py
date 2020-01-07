'''
Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.
'''
#recursive way to solve function

# Returns the count of ways we can sum 
# S[0...m-1] coins to get sum n 
def count(S, m, n ): 

	# If n is 0 then there is 1 
	# solution (do not include any coin) 
	if (n == 0): 
		print("n=0. Return 1")
		return 1

	# If n is less than 0 then no 
	# solution exists 
	if (n < 0): 
		print("n<0. Return 0")
		return 0

	# If there are no coins and n 
	# is greater than 0, then no 
	# solution exist 
	if (m <=0 and n >= 1): 
		print("m <=0 and n >= 1. Return 0")
		return 0

	# count is sum of solutions 
	# (i) including S[m-1] 
	# (ii) excluding S[m-1] 
	a = count( S, m - 1, n )
	b = count( S, m, n-S[m-1])
	print("Returning a+b = ",str(a+b))
	return a+b

# Driver program to test above function 
arr = [1, 2, 3] 
m = len(arr) 
# print(count(arr, m, 4)) 


# A dynamic programming based function 

def dp_count(S, m, n): 
	# We need n+1 rows as the table is constructed 
	# in bottom up manner using the base case 0 value 
	# case (n = 0) 
	table = [[0 for x in range(m)] for x in range(n+1)] 

	# Fill the entries for 0 value case (n = 0) 
	for i in range(m): 
		table[0][i] = 1

	# Fill rest of the table entries in bottom up manner 
	for i in range(1, n+1): 
		for j in range(m): 

			# Count of solutions including S[j] 
			x = table[i - S[j]][j] if i-S[j] >= 0 else 0

			# Count of solutions excluding S[j] 
			y = table[i][j-1] if j >= 1 else 0

			# total count 
			table[i][j] = x + y 

	return table[n][m-1] 

# Driver program to test above function 
arr = [1, 2, 3] 
m = len(arr) 
n = 4
print(dp_count(arr, m, n)) 

