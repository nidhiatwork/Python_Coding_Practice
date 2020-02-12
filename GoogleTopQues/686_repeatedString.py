'''
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").'''
import math
def repeatedStringMatch(A,B):
    times = -(-len(B) // len(A))
    for i in range(2):
        if B in (A * (times + i)):
            return times + i
    return -1

A="abc"
B="cabcabca"
print(repeatedStringMatch(A,B))