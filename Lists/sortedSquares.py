'''
return squares of a list in ascending order. It might have negatives
'''


from collections import deque

def sortedSquares(A):
    # one way is: return sorted([a*a for a in A])

    answer = deque()
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

nums = [-7,-3,2,3,11]
print(sortedSquares(nums))