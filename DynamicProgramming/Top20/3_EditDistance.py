'''
Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.

Insert
Remove
Replace
All of the above operations are of equal cost.

Examples:

Input:   str1 = "geek", str2 = "gesek"
Output:  1
We can convert str1 into str2 by inserting a 's'.

Input:   str1 = "cat", str2 = "cut"
Output:  1
We can convert str1 into str2 by replacing 'a' with 'u'.

Input:   str1 = "sunday", str2 = "saturday"
Output:  3
m: Length of str1 (first string)
n: Length of str2 (second string)
If last characters of two strings are same, nothing much to do. Ignore last characters and get count for remaining strings. So we recur for lengths m-1 and n-1.
Else (If last characters are not same), we consider all operations on ‘str1’, consider all three operations on last character of first string, recursively compute minimum cost for all three operations and take minimum of three values.
Insert: Recur for m and n-1
Remove: Recur for m-1 and n
Replace: Recur for m-1 and n-1
'''
#recursive way to solve function
def editDistance(str1,str2,m,n): 
	# If first string is empty, the only option is to 
    # insert all characters of second string into first 
	if m==0: 
		return n
  
    # If second string is empty, the only option is to 
    # remove all characters of first string 
	if n==0: 
		return m

	if str1[m-1] == str2[n-1]:
    		return editDistance(str1,str2,m-1,n-1)
	else:
    		return 1 + min(editDistance(str1,str2,m,n-1), editDistance(str1,str2,m-1,n), editDistance(str1,str2,m-1,n-1))  

# Driver Program to test above function
str1="sunday"
str2="saturday"
m=len(str1)
n=len(str2)
print(editDistance(str1,str2,m,n))

# A dynamic programming based function 
def editDistDP(str1, str2, m, n): 
	# Create a table to store results of subproblems 
	dp = [[0 for x in range(n+1)] for x in range(m+1)] 

	# Fill d[][] in bottom up manner 
	for i in range(m+1): 
		for j in range(n+1): 

			# If first string is empty, only option is to 
			# insert all characters of second string 
			if i == 0: 
				dp[i][j] = j # Min. operations = j 

			# If second string is empty, only option is to 
			# remove all characters of second string 
			elif j == 0: 
				dp[i][j] = i # Min. operations = i 

			# If last characters are same, ignore last char 
			# and recur for remaining string 
			elif str1[i-1] == str2[j-1]: 
				dp[i][j] = dp[i-1][j-1] 

			# If last character are different, consider all 
			# possibilities and find minimum 
			else: 
				dp[i][j] = 1 + min(dp[i][j-1],	 # Insert 
								dp[i-1][j],	 # Remove 
								dp[i-1][j-1]) # Replace 

	return dp[m][n] 

# Driver program 
str1 = "sunday"
str2 = "saturday"

print(editDistDP(str1, str2, len(str1), len(str2))) 
