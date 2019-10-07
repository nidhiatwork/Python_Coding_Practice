'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
'''
#To do
def wordBreak(s, words):
    dp = [False] * (len(s) + 1) # dp[i] means s[:i+1] can be segmented into words in the wordDicts 
    dp[0] = True
    for i in range(len(s)):
        for j in range(i, len(s)):
            print("s[i: j+1] is: ",s[i: j+1])
            if dp[i] and s[i: j+1] in wordDict:
                print(s[i: j+1]+" is in wordDict")
                print("Set dp[{}] to True".format(j+1))
                dp[j+1] = True
                
    return dp[-1]

s = "aaaaaaa"
wordDict = ["aaaa","aaa"]

# s = "leetcode"
# wordDict = ["leet", "code"]
print(wordBreak(s, wordDict))