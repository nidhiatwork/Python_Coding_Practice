'''
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
'''

def do(S):
    letter_pos = {c:i for i,c in enumerate(S)}
    left,right = 0,0
    ans = []
    for i,c in enumerate(S):
        right = max(right, letter_pos[c])
        if i==right:
            ans.append(right-left+1)
            left = i+1
    return ans
    
    
print(do("ababcbacadefegdehijhklij"))
