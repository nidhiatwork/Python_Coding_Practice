'''
Card points are given in the integer array cardPoints. In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards. Your score is the sum of the points of the cards you have taken. Maximize the points
'''

def maxScore(cardPoints, k):
    n = len(cardPoints)
    lSum = 0
    for i in range(k):
        lSum += cardPoints[i]
    
    mx = lSum
    rSum=0
    for i in range(k):
        rSum += cardPoints[n-1-i]
        lSum -= cardPoints[k-1-i]
        mx = max(mx,lSum+rSum)
    
    return mx
print(maxScore([1,79,80,1,1,1,200,1],3))