'''
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
'''


def knapSack(W, wt, val, n):
    if n==0 or W == 0:
        return 0
    if wt[n-1]>W:
        return knapSack(W, wt, val, n-1)
    else:
        return max(knapSack(W, wt, val, n-1), val[n-1]+knapSack(W-wt[n-1], wt, val, n-1))

def knapSack_dp(W, wt, val, n):
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]
 
    # Build table K[][] in bottom up manner
    for item in range(n + 1):
        for w in range(W + 1):
            if item == 0 or w == 0:
                dp[item][w] = 0
            elif wt[item-1] <= w:
                dp[item][w] = max(val[item-1]
                          + dp[item-1][w-wt[item-1]],  
                              dp[item-1][w])
            else:
                dp[item][w] = dp[item-1][w]

    return dp[n][W]
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack_dp(W, wt, val, n))
