'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
'''
from collections import deque

def plusOne_usingDeque(digits):
  if digits[-1]!=9:
        return digits[:-1]+[digits[-1]+1]
  else:
        ans = deque()
        carry=1
        while digits:
              ans.appendleft((digits[-1]+carry)%10)
              carry = (digits[-1]+carry)//10
              digits.pop()
        if carry:
              ans.appendleft(1)
  return list(ans)

def plusOne_usingRecursion(digits):
        if digits == []:  #just for case: digits = [9]
            return [1]
        if digits[-1] != 9:
            return digits[:-1]+[digits[-1]+1]
        else:
            return plusOne_usingRecursion(digits[:-1])+[0]

digits = [1,9,9]
print(plusOne_usingDeque(digits))