'''
Given a distance ‘dist, count total number of ways to cover the distance with 1, 2 and 3 steps.
Input:  n = 3
Output: 4
Below are the four ways
 1 step + 1 step + 1 step
 1 step + 2 step
 2 step + 1 step
 3 step

Input:  n = 4
Output: 7

Suppose you have distance 'dist' to cover, then you can hop either 1 step, 2 step, 3 step.
1. If you hop 1 step then remaining distance = dist-1
2. If you hop 2 step then remaining distance = dist-2
3. If you hop 3 step then remaining distance = dist-3
'''
#recursive way #1 to solve function
def findStep( n) : 
	if (n == 1 or n == 0) :
		return 1
	elif (n == 2) : 
		return 2
	else : 
		return findStep(n - 3) + findStep(n - 2) + findStep(n - 1)  

# Driver code 
n = 2
# print(findStep(n))

#recursive way #2 to solve function
def printCountRec(dist): 
      
    # Base cases 
    if dist < 0: 
        return 0
          
    if dist == 0:
        return 1
  
    # Recur for all previous 3 add the results 
    return (printCountRec(dist-1) + printCountRec(dist-2) + printCountRec(dist-3))

dist = 4
# print(printCountRec(dist)) 

# A dynamic programming based function 
def dp_func(n): 
	dp = [0]*(n+1)
	dp[0] = 1
	dp[1] = 1
	dp[2] = 2
	for i in range(3,n+1):
    		dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
	return dp[n]

# Driver code 
print(dp_func(4))