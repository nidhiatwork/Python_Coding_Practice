'''
Given two positive integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.

Return a list of all powerful integers that have value less than or equal to bound.

You may return the answer in any order.  In your answer, each value should occur at most once.

 
Example 1:

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation: 
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2
'''

def powerfulIntegers(x, y, bound):
    ans = set()
    # 2**18 > bound
    for i in range(18):
        for j in range(18):
            v = x**i + y**j
            if v <= bound:
                ans.add(v)
    return list(ans)

print(powerfulIntegers(2,3,10))