'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
'''
import collections
def plusOne_1(digits):
    carry = 1
    ans = collections.deque()
    for i in range(len(digits)-1,-1,-1):
        if(digits[i]+carry)>9:
            ans.appendleft(0)
            carry=1
        else:
            ans.appendleft(digits[i]+carry)
            carry=0
    if carry==1: 
        ans.appendleft(1)
    return list(ans)
    

digits = [9,9,4]
print(plusOne_1(digits))
