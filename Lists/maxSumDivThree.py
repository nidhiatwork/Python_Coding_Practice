'''Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.
[3,6,5,1,8] -> 18
'''
def maxSumDivThree(A):
		dp = [0]
		for a in A:
			for d in dp[:]:
				if (d + a) % 3==0:
					dp[(d + a) % 3] = max(dp[(d + a) % 3], d + a)
		return dp[0]

nums = [3,6,5,1,8]
print(maxSumDivThree(nums))
