'''
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
Input: [4,2,5,7]
Output: [4,5,2,7]
'''

def sortArrayByParityII_1(A):
      
  evens = [a for a in A if a%2==0]
  odds = [a for a in A if a%2==1]
  i=0
  for e,o in zip(evens,odds):
        A[i]=e
        A[i+1]=o
        i+=2
  return A

def sortArrayByParityII_2(self, A):
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A

A = [4,2,5,7]
print(sortArrayByParityII_1(A))