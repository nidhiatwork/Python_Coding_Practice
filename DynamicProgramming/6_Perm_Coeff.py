'''
Permutation refers to the process of arranging all the members of a given set to form a sequence. The number of permutations on a set of n elements is given by n! , where “!” represents factorial.
The Permutation Coefficient represented by P(n, k) is used to represent the number of ways to obtain an ordered subset having k elements from a set of n elements.

Mathematically it’s given as:
nPk = n! / (n-k)! = n.(n-1).(n-2)...(n-k+1)

The coefficient can also be computed recursively using the below recursive formula:

P(n, k) = P(n-1, k) + k* P(n-1, k-1)   
'''
#recursive way to solve function
def my_permutationCoeff(n,k): 
	if n<k:
    		return 1
	else:
    		return n*my_permutationCoeff(n-1,k)

# Driver Program to test above function 
print(my_permutationCoeff(5,3))

# A O(n) solution that uses table fact[] to calculate the Permutation Coefficient 

def dp_permutationCoeff(n, k): 
	fact = [0 for i in range(n + 1)] 

	# base case 
	fact[0] = 1

	# Calculate value 
	# factorials up to n 
	for i in range(1, n + 1): 
		fact[i] = i * fact[i - 1] 

	# P(n, k) = n!/(n-k)! 
	return int(fact[n] / fact[n - k]) 

# Driver Code 
n = 5
k = 3
print("Value of P(", n, ", ", k, ") is ", 
		dp_permutationCoeff(n, k), sep = "") 

# A O(n) time and O(1) extra space solution to calculate the Permutation Coefficient 

def dp2_PermutationCoeff(n, k): 
	Fn = 1

	# Compute n! and (n-k)! 
	for i in range(1, n + 1): 
		Fn *= i 
		if (i == n - k): 
			Fk = Fn 

	coeff = Fn // Fk 
	return coeff 

# Driver Code 
n = 5
k = 3
print("Value of P(", n, ", ", k, ") is ", 
	dp2_PermutationCoeff(n, k), sep = "") 


