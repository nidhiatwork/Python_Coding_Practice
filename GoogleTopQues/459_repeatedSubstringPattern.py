'''
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
'''

def repeatedSubstringPattern(s):
    f_char = s[0]
    ss=f_char
    for i in range(1,len(s)):
        if s[i]!=f_char:
            ss+=s[i]
        else:
            j=i
            flag = True
            while j< len(s):
                if s[j:j+len(ss)]!=ss:
                    flag = False
                    ss+=s[i]
                    break
                else:
                    j+=len(ss)
            if flag:
                return True
    return False


s = "aba"
print(repeatedSubstringPattern(s))
