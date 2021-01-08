'''In an array A of 0s and 1s, how many non-empty subarrays have sum S?

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
'''
#Todo
import collections
def numSubarraysWithSum(A, S):
    P = [0]
    for x in A: 
        P.append(P[-1] + x)
    count = collections.Counter()

    ans = 0
    for x in P:
        ans += count[x]
        count[x + S] += 1

    return ans     
            
A = [1,0,1,0,1]
S = 2
print(numSubarraysWithSum(A, S))