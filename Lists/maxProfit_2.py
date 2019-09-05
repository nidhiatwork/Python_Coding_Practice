'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
'''
import sys
def maxProfit_1(prices):
    n = len(prices)
    max = 0
    for i in range(n):
        for j in range(i+1,n):
            diff = prices[j]-prices[i]
            if diff > max:
                max = diff
    return max
'''
We need to find the largest peak following the smallest valley. We can maintain two variables - minprice and maxprofit corresponding to the smallest valley and maximum profit (maximum difference between selling price and minprice) obtained so far respectively.
'''
def maxProfit_2(prices):
    n = len(prices)
    min,max =sys.maxsize,0
    for i in range(n):
        if (prices[i] < min):
            min = prices[i]
        elif (prices[i] - min) > max:
            max = prices[i] - min
    
    return max

prices = [3,2,6,5,0,3]
print(maxProfit_2(prices))