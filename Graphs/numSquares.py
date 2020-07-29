'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
'''
#To do

def numSquares(n):

    if n < 2:
        return n
    lst = []
    i = 1
    while i * i <= n:
        lst.append( i * i )
        i += 1
    cnt = 0
    toCheck = {n}
    while toCheck:
        cnt += 1
        temp = set()
        for x in toCheck:
            for y in lst:
                if x == y:
                    return cnt
                if x < y:
                    break
                temp.add(x-y)
        toCheck = temp
        print("to check: ",toCheck)

    return cnt

import sys
def numSquares_1(n):
    if (n <= 0):
        return 0
        
    # // cntPerfectSquares[i] = the least number of perfect square numbers 
    # // which sum to i. Note that cntPerfectSquares[0] is 0.
    cntPerfectSquares=[sys.maxsize]*(n+1)
    cntPerfectSquares[0] = 0
    for i in range(1,n+1):
        # // For each i, it must be the sum of some number (i - j*j) and 
        # // a perfect square number (j*j).
        j = 1
        while j*j <= i:
            cntPerfectSquares[i] = min(cntPerfectSquares[i], cntPerfectSquares[i - j*j] + 1)
            j+=1
    return cntPerfectSquares[-1]

print(numSquares(12))