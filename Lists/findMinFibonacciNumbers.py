'''Given the number k, return the minimum number of Fibonacci numbers whose sum is equal to k, whether a Fibonacci number could be used multiple times.

Input: k = 19
Output: 3 
Explanation: For k = 19 we can use 1 + 5 + 13 = 19.
'''

def findMinFibonacciNumbers(k):
    vals = []
    a,b=0,1
    while b<=k:
        vals.append(b)
        a,b=b,a+b
    n = len(vals)
    ans=0
    for i in range(n-1,-1,-1):
        if(vals[i]<=k):
            ans+=1
            k-=vals[i]
        if(k==0):
            return ans
    return ans

k = 5
print(findMinFibonacciNumbers(k))