'''
Find length of longest subarray which has alternating increasing and decreasing values
Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
'''

class Solution:
    def maxTurbulenceSize(self, A) -> int:
        N = len(A)
        ans = 1
        anchor = 0

        for i in range(1, N):
            c = self.cmp(A[i-1], A[i])
            if c == 0:
                anchor = i
            elif i == N-1 or c * self.cmp(A[i], A[i+1]) != -1:
                ans = max(ans, i - anchor + 1)
                anchor = i
        return ans
    
    def cmp(self,a,b):
        if a>b:
            return 1
        elif a<b:
            return -1
        return 0