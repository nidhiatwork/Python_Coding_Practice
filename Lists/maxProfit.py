'''Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
'''
def maxProfit(prices):
    maxprofit = 0
    for i in range(1, len(prices)):
        if (prices[i] > prices[i - 1]):
            print("Adding profit: ",prices[i] - prices[i - 1])
            maxprofit += prices[i] - prices[i - 1]
    return maxprofit



price = [1,2,3,5]
print(maxProfit(price))