'''
LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”.
Examples:
1) Consider the input strings “AGGTAB” and “GXTXAYB”. Last characters match for the strings. So length of LCS can be written as:
L(“AGGTAB”, “GXTXAYB”) = 1 + L(“AGGTA”, “GXTXAY”)
longest-common-subsequence
2) Consider the input strings “ABCDGH” and “AEDFHR. Last characters do not match for the strings. So length of LCS can be written as:
L(“ABCDGH”, “AEDFHR”) = MAX ( L(“ABCDG”, “AEDFHR”), L(“ABCDGH”, “AEDFH”) )
'''
#recursive way to solve function

def lcs(X, Y, m, n): 

	if m == 0 or n == 0: 
		return 0 
	elif X[m-1] == Y[n-1]: 
		return 1 + lcs(X, Y, m-1, n-1)
	else: 
		return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))


# Driver program to test the above function 
X = "AGGTAB"
Y = "GXTXAYB"
# print("Length of LCS is ", lcs(X , Y, len(X), len(Y))) 


# Dynamic Programming implementation of LCS problem 

def dp_lcs(X , Y): 
	# find the length of the strings 
	m = len(X) 
	n = len(Y) 

	# declaring the array for storing the dp values 
	L = [[None]*(n+1) for i in range(m+1)] 

	"""Following steps build L[m+1][n+1] in bottom up fashion 
	Note: L[i][j] contains length of LCS of X[0..i-1] 
	and Y[0..j-1]"""
	for i in range(m+1): 
		for j in range(n+1): 
			if i == 0 or j == 0 : 
				L[i][j] = 0
			elif X[i-1] == Y[j-1]: 
				L[i][j] = L[i-1][j-1]+1
			else: 
				L[i][j] = max(L[i-1][j] , L[i][j-1]) 

	# Following code is used to print LCS 
	index = L[m][n] 
  
    # Create a character array to store the lcs string 
	lcs = [""] * (index+1) 
	lcs[index] = "" 
  
    # Start from the right-most-bottom-most corner and 
    # one by one store characters in lcs[] 
	i = m 
	j = n 
	while i > 0 and j > 0: 

	    # If current character in X[] and Y are same, then 
	    # current character is part of LCS 
		if X[i-1] == Y[j-1]: 
			lcs[index-1] = X[i-1] 
			i-=1
			j-=1
			index-=1
 
        # If not same, then find the larger of two and 
        # go in the direction of larger value 
		elif L[i-1][j] > L[i][j-1]: 
			i-=1
		else: 
			j-=1
  
	print("LCS of " + X + " and " + Y + " is " + "".join(lcs)) 
   
#end of function lcs 


# Driver program to test the above function 
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", dp_lcs(X, Y))