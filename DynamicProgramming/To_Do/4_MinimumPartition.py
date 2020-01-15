'''
Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum.
If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2 must have n-m elements and the value of abs(total(Subset1) – total(Subset2)) should be minimum.

Input:  arr[] = {1, 6, 11, 5} 
Output: 1
Explanation:
Subset1 = {1, 5, 6}, total of Subset1 = 12 
Subset2 = {11}, total of Subset2 = 11   
To generate sums we either include the i’th item in set 1 or don’t include, i.e., include in set 2.
'''
import sys
#recursive way to solve function
def findMinRec(arr,i,sumCalculated,sumTotal): 
	# # If we have reached last element. 
	# # Sum of one subset is sumCalculated, 
	# # total of other subset is sumTotal- 
	# # sumCalculated. Return absolute 
	# # difference of two sums. 
	print("arr=",arr," i=",i," sumCalculated=",sumCalculated," sumTotal=",sumTotal)
	if (i == 0):
		return abs((sumTotal-sumCalculated) - sumCalculated)

	# # For every item arr[i], we have two choices 
	# # (1) We do not include it first set 
	# # (2) We include it in first set 
	# # We return minimum of two choices 
	a = findMinRec(arr, i - 1, sumCalculated + arr[i-1], sumTotal)
	b = findMinRec(arr, i-1, sumCalculated, sumTotal)
	print("Returning min of ",a," and ",b,"=",min(a,b))
	return min(a,b)

arr = [3, 1, 4, 2, 2, 1]
n = len(arr)
# print("The minimum difference between two sets is " + str(findMinRec(arr, n, 0,sum(arr))))  

# A dynamic programming based function 
def findMin(arr,n):
		total = sum(arr)
		dp = [[False for i in range(total+1)]for j in range(n+1)]
		# Initialize first column as true.  
        # 0 sum is possible  with all elements. 
		for i in range(n+1):
			dp[i][0] = True 

		# Initialize top row, except dp[0][0],  
        # as false. With 0 elements, no other  
        # sum except 0 is possible 
		for i in range(1,total+1):
			dp[0][i] = False 
		
		# Fill the partition table  
        # in bottom up manner 
		for i in range(1,n+1):
			for j in range(1,total+1):
				# If i'th element is excluded 
				dp[i][j] = dp[i - 1][j]
				
				# If i'th element is included 
				if (arr[i - 1] <= j):
					dp[i][j] |= dp[i - 1][j - arr[i - 1]]
			
		diff = sys.maxsize
		# Find the largest j such that dp[n][j] 
        # is true where j loops from sum/2 t0 0 
		for j in range(total//2,-1,-1):
		
			if (dp[n][j] == True):
				diff = total - 2 * j
				break
		 
		return diff
	
	
arr = [1,3,2] 
n = len(arr)
print("The minimum difference between 2 sets is "+ str(findMin(arr, n)))
