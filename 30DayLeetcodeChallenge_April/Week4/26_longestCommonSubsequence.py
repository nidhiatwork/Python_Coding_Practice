'''Given two strings text1 and text2, return the length of their longest common subsequence.
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
'''
def longestCommonSubsequence_recursive(x,y,i,j):
    if i<=0 or j<=0:
        return 0
    if x[i-1]==y[j-1]:
        return 1+longestCommonSubsequence_recursive(x,y,i-1,j-1)
    else:
        return max(longestCommonSubsequence_recursive(x,y,i-1,j),longestCommonSubsequence_recursive(x,y,i,j-1))

def longestCommonSubsequence_memo(x,y,i,j,dp):
    if not dp[i][j]:
        if i<=0 or j<=0:
            dp[i][j] =0
        elif x[i-1]==y[j-1]:
            dp[i][j]= 1+longestCommonSubsequence_memo(x,y,i-1,j-1,dp)
        else:
            dp[i][j]=  max(longestCommonSubsequence_memo(x,y,i-1,j,dp),longestCommonSubsequence_memo(x,y,i,j-1,dp))
    return dp[i][j]

def longestCommonSubsequence_dp(text1: str, text2: str) -> int:
        n,m=len(text1),len(text2)
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                if text1[i]==text2[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
        return dp[-1][-1]

s1,s2 =  "nidhi", "nidfhasdkfd"
dp = [[None for i in range(len(s2)+1)]for i in range(len(s1)+1)]
print(longestCommonSubsequence_memo(s1, s2, len(s1), len(s2), dp))