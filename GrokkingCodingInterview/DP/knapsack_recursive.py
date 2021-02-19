'''
Let’s take the example of Merry, who wants to carry some fruits in the knapsack to get maximum profit. Here are the weights and profits of the fruits:

Items: { Apple, Orange, Banana, Melon }
Weights: { 2, 3, 1, 4 }
Profits: { 4, 5, 3, 7 }
Knapsack capacity: 5
'''

from collections import Counter
def knapsack_recursive(profits,weights,capacity):
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profits)+1)]
    return solve(profits,weights,capacity, len(profits), dp)

def solve(profits,weights,capacity, idx, dp):
    if idx==0 or capacity==0:
        return 0
    if dp[idx][capacity]!=-1:
        return dp[idx][capacity]
    if weights[idx-1]<=capacity:
        dp[idx][capacity] = max(profits[idx-1]+ solve(profits, weights,capacity-weights[idx-1], idx-1, dp), solve(profits, weights,capacity, idx-1, dp))
        return dp[idx][capacity]
    elif weights[idx-1]>capacity:
        dp[idx][capacity] = solve(profits, weights,capacity, idx-1, dp)
        return dp[idx][capacity]

Weights = [10, 20, 30] 
Profits = [60, 100, 120] 
print(knapsack_recursive(Profits,Weights,50))
