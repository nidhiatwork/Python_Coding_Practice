'''
Chef recently graduated Computer Science in university, so he was looking for a job. He applied for several job offers, but he eventually settled for a software engineering job at ShareChat. Chef was very enthusiastic about his new job and the first mission assigned to him was to implement a message encoding feature to ensure the chat is private and secure.

Chef has a message, which is a string S with length N containing only lowercase English letters. It should be encoded in two steps as follows:

Swap the first and second character of the string S, then swap the 3rd and 4th character, then the 5th and 6th character and so on. If the length of S is odd, the last character should not be swapped with any other.
Replace each occurrence of the letter 'a' in the message obtained after the first step by the letter 'z', each occurrence of 'b' by 'y', each occurrence of 'c' by 'x', etc, and each occurrence of 'z' in the message obtained after the first step by 'a'.
Input:
2
9
sharechat
4
chef
Output:
shizxvzsg
sxuv
'''

def encodeString(l,s):
    i=0
    s_list = list(s)
    while i<l-1:
        s_list[i],s_list[i+1] = s_list[i+1],s_list[i]
        i+=2
    print("After round1: ",''.join(s_list))
    for i,c in enumerate(s_list):
        s_list[i]=chr(122-ord(c)+97)
    return ''.join(s_list)


T = int(input())
ans = []
while T:
    l = int(input())
    s = input()
    ans.append(encodeString(l,s))
    T-=1
print('\n'.join(ans))