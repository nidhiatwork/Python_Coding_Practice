'''
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
Example:

Input:  set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.

The isSubsetSum problem can be divided into two subproblems
…a) Include the last element, recur for n = n-1, sum = sum – set[n-1]
…b) Exclude the last element, recur for n = n-1.
If any of the above the above subproblems return true, then return true

isSubsetSum(set, n, sum) = isSubsetSum(set, n-1, sum) || 
                           isSubsetSum(set, n-1, sum-set[n-1])
Base Cases:
isSubsetSum(set, n, sum) = false, if sum > 0 and n == 0
isSubsetSum(set, n, sum) = true, if sum == 0 
'''
#recursive way to solve function
def isSubsetSum(S, n, sum):
	if sum!=0 and n==0:
			return False
	if sum==0:
			return True
	if (S[n - 1] > sum) : 
        	return isSubsetSum(S, n - 1, sum)
	
	return isSubsetSum(S,n-1,sum) or isSubsetSum(S,n-1,sum-S[n-1])

# Driver Program to test above function 
S = [3, 34, 4, 12, 5, 2]
sum = 9
n = len(S)
print(isSubsetSum(S, n, sum))

# A dynamic programming based function 

def dp_isSubsetSum(S,n,sum): 
	
	# The value of subset[i][j] will be 
	# true if there is a 
	# subset of set[0..j-1] with sum equal to i 
	subset=([[False for i in range(sum+1)] 
			for i in range(n+1)]) 
	
	# If sum is 0, then answer is true 
	for i in range(n+1): 
		subset[i][0] = True
		
		# If sum is not 0 and set is empty, 
		# then answer is false 
		for i in range(1,sum+1): 
			subset[0][i]=False
			
		# Fill the subset table in botton up manner 
		for i in range(1,n+1): 
			for j in range(1,sum+1): 
				if j<S[i-1]: 
					subset[i][j] = subset[i-1][j] 
				if j>=S[i-1]: 
					subset[i][j] = (subset[i-1][j] or
								subset[i - 1][j-S[i-1]]) 
	
		# uncomment this code to print table 
		# for i in range(n+1): 
		# for j in range(sum+1): 
		#	 print (subset[i][j],end=" ") 
		# print() 
	return subset[n][sum] 
		
S = [3, 34, 4, 12, 5, 2] 
sum = 9
n =len(S) 
if (dp_isSubsetSum(S, n, sum) == True): 
	print("Found a subset with given sum") 
else: 
	print("No subset with given sum") 
	