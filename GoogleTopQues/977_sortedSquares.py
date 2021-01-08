'''
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
'''
import collections
def sortedSquares_1(A):
    ans=[]
    i,j=0,len(A)-1
    while i<=j:
        if abs(A[i])<abs(A[j]):
            ans.append(A[j]**2)
            j-=1
        else:
            ans.append(A[i]**2)
            i+=1
    return ans[::-1]

def sortedSquares_2(A):
    answer = collections.deque()
    l, r = 0, len(A) - 1
    while l <= r:
        left, right = abs(A[l]), abs(A[r])
        if left > right:
            answer.appendleft(left * left)
            l += 1
        else:
            answer.appendleft(right * right)
            r -= 1
    return list(answer)

def sortedSquares_3( A):
    answer = [0] * len(A)
    l, r = 0, len(A) - 1
    while l <= r:
        left, right = abs(A[l]), abs(A[r])
        if left > right:
            answer[r - l] = left * left
            l += 1
        else:
            answer[r - l] = right * right
            r -= 1
    return answer

A = [-4,-1,0,3,10]
print(sortedSquares_1(A))
