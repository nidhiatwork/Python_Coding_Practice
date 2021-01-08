'''
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
 
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 
 '''

def findComplement_brute(num):
    b_num = bin(num)[2:]
    ans = ""
    for bit in b_num:
        ans = ans+'1' if bit=='0' else ans+'0'
    return int(ans,2)

def findComplement_XOR(num):
        i = 1
        while num >= i:
            num ^= i
            i <<= 1
        return num
num = 5
print(findComplement_XOR(num))