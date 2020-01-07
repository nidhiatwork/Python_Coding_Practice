'''
Write a function that takes two parameters n and k and returns the value of Binomial Coefficient C(n, k). For example, your function should return 6 for n = 4 and k = 2, and it should return 10 for n = 5 and k = 2.

C(n, k) = C(n-1, k-1) + C(n-1, k)
C(n, 0) = C(n, n) = 1
'''
#recursive way to solve function
def binomialCoeff(n,k): 
	if k==0 or k==n:
		return 1
	return binomialCoeff(n-1,k-1) + binomialCoeff(n-1,k)  

# Driver Program to test above function 
# print(binomialCoeff(4,2))

# A dynamic programming based function 
def dp1_binomialCoeff(n,k): 
	binomials = [[0 for i in range(n+1)] for _ in range(n+1)]
	for i in range(n+1):
		for j in range(i+1): 
			#Since you dont need i above k, you can instead use range (min(i, k)+1)
			if j==0 or j==n:
				binomials[i][j]=1
			else:
				binomials[i][j] = binomials[i-1][j-1] + binomials[i-1][j]
	return binomials[n][k]		

# Driver code 
print(dp1_binomialCoeff(4,2))

#DP method with space optimised. We update the same one-D array for all values of n,k. Instead of maintaining whole 2-D matrix
def dp2_binomialCoeff(n , k):
    # Declaring an empty array 
    C = [0 for i in range(k+1)] 
    C[0] = 1 #since nC0 is 1 
  
    for i in range(1,n+1): 
  
        # Compute next row of pascal triangle using 
        # the previous row 
        j = min(i ,k) 
        while (j>0): 
            C[j] = C[j] + C[j-1] 
            j -= 1
    return C[k] 

print(dp2_binomialCoeff(4,2))