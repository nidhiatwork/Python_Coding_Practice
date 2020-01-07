'''
Given n friends, each one can remain single or can be paired up with some other friend. Each friend can be paired only once. Find out the total number of ways in which friends can remain single or can be paired up.

Examples :

Input  : n = 3
Output : 4

Explanation
{1}, {2}, {3} : all single
{1}, {2, 3} : 2 and 3 paired but 1 is single.
{1, 2}, {3} : 1 and 2 are paired but 3 is single.
{1, 3}, {2} : 1 and 3 are paired but 2 is single.
Note that {1, 2} and {2, 1} are considered same.
For n-th person there are two choices:
1) n-th person remains single, we recur 
   for f(n - 1)
2) n-th person pairs up with any of the 
   remaining n - 1 persons. We get (n - 1) * f(n - 2)

Therefore we can recursively write f(n) as:
f(n) = f(n - 1) + (n - 1) * f(n - 2)
'''
# Via recursion
def countFriendsPairings(n): 
	if n<=2:
    		return n
	else:
    		return countFriendsPairings(n-1) + (n-1)*countFriendsPairings(n-2)
    		
# Driver code 
n = 4
# print(countFriendsPairings(n)) 

# A dynamic programming based function 
def dp_countFriendsPairings(n): 

	dp = [0 for i in range(n + 1)] 

	# Filling dp[] in bottom-up manner using 
	# recursive formula explained above. 
	for i in range(n + 1): 
		if(i <= 2): 
			dp[i] = i 
		else: 
			dp[i] = dp[i - 1] + (i - 1) * dp[i - 2] 
	return dp[n] 

# Driver code 
n = 4
# print(dp_countFriendsPairings(n)) 

#Via DP with space optimised
def dp2_countFriendsPairings(n):
	if n<=2: 
		return n
	a=1
	b=2
	for i in range(3,n+1):
		c = b + (i-1)*a
		a=b
		b=c
	return b

# Driver code 
n = 4
print(dp2_countFriendsPairings(n)) 
