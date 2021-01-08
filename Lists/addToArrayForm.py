'''
For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.
Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
'''

def addToArrayForm(A, K):
        A[-1] += K
        for i in range(len(A) - 1, -1, -1):
            carry = A[i]//10
            A[i] = A[i]%10
            if i: A[i-1] += carry
        while carry:
            A = [carry%10] + A
            carry//=10
        return A

A = [2,5,9]
K = 42
print(addToArrayForm(A,K))