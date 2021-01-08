'''
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
p
Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
'''

#To do
def isMatch_YT(s,p):
    s, p = ' '+ s, ' '+ p
    lenS, lenP = len(s), len(p)
    dp = [[0]*(lenP) for i in range(lenS)]
    dp[0][0] = 1

    for j in range(1, lenP):
        if p[j] == '*':
            dp[0][j] = dp[0][j-2]

    for i in range(1, lenS):
        for j in range(1, lenP):
            if p[j] in {s[i], '.'}:
                dp[i][j] = dp[i-1][j-1]
            elif p[j] == "*":
                dp[i][j] = dp[i][j-2] or int(dp[i-1][j] and p[j-1] in {s[i], '.'})

    return bool(dp[-1][-1])

def isMatch(text,pattern):
    memo = {}
    def dp(i, j):
        if (i, j) not in memo:
            if j == len(pattern):
                ans = i == len(text)
            else:
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    ans = dp(i, j+2) or first_match and dp(i+1, j)
                else:
                    ans = first_match and dp(i+1, j+1)

            memo[i, j] = ans
        return memo[i, j]

    return dp(0, 0)

s = ['aa','aa','ab','aab','mississippi']
p = ['a','a*','.*','c*a*b','mis*is*ip*.']
print(isMatch_YT(s[4],p[4]))
# for i in range(5):
#     print(isMatch(s[i],p[i]))