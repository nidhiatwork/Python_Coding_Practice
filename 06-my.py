"""Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""

def compress_s(s):
    if not s or len(s)==1:
        return s
    ans = ""
    count = 1
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count+=1
        else:
            ans+=s[i]+str(count)
            count=1
    ans+=s[i+1]+str(count)
    return ans if len(ans)<len(s) else s


print(compress_s("seee"))