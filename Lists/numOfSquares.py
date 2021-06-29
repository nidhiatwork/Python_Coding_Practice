'''
Given an integer A representing the number of square blocks. The height of each square block is 1. The task is to create a staircase of max height using these blocks.

The first stair would require only one block, the second stair would require two blocks and so on.

Find and return the maximum height of the staircase.



Pro
i/p -  A = 10
o/p - 4
'''
probable_answer = 0
def findHeight(s, l, h):
    global probable_answer
    while l<=h:
        mid = (l+h)//2
        num_squares = (mid*(mid+1))//2
        if num_squares<s:
            l=mid+1
            probable_answer = max(probable_answer, mid)
        elif num_squares>s:
            h=mid-1
        else:
            return mid
    return probable_answer

s = 15
print(findHeight(s, l=1, h=s))