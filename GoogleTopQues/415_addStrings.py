'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

def addStrings_usingList(num1, num2):
    num1, num2 = list(num1), list(num2)
    carry, res = 0, []
    while len(num2) > 0 or len(num1) > 0:

        n1 = int(num1.pop()) if len(num1) > 0 else 0
        n2 = int(num2.pop()) if len(num2) > 0 else 0

        temp = n1 + n2 + carry 
        res.append(str(temp % 10))
        carry = temp // 10
    if carry: 
        res.append(str(carry))
    return ''.join(res)[::-1]

num1 = "572"
num2 = "76543"
print(addStrings_usingList(num1, num2))
