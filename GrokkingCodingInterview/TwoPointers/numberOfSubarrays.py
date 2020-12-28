'''
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
'''

def numberOfSubarrays(A, k):
    i = count = res = 0
    for j in range(len(A)):
        if A[j] & 1:
            k -= 1
            count = 0
        while k == 0:
            k += A[i] & 1
            i += 1
            count += 1
        res += count
    return res

def numberOfSubarrays_1(A, k):
    dic = { 0: 1 }
    cnt = res = 0
    for num in A:
        if num % 2 == 1:
            cnt += 1

        if cnt - k in dic:
            res += dic[cnt-k]

        dic[cnt] = dic.get(cnt, 0) + 1

    return res

A = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(numberOfSubarrays_1(A,k))
