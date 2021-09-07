# you can write to stdout for debugging purposes, e.g.
print("This is a debug message")

import collections
def getHint(secret: str, guess: str) -> str:
    bulls,cows=0,0
    s_pointer, g_pointer = 0,0
    s_array, g_array=[],[]
    while s_pointer<len(secret):
        if secret[s_pointer]==guess[g_pointer]:
            bulls+=1
        else:
            s_array.append(secret[s_pointer])
            g_array.append(guess[g_pointer])
        s_pointer+=1
        g_pointer+=1
    print(s_array)
    print(g_array)
    s_counter = collections.Counter(s_array)
    g_counter = collections.Counter(g_array)
    for k,v in s_counter.items():
        if not k in g_counter or g_counter[k]==0:
            continue
        else:
            while v and g_counter[k]>0:
                g_counter[k]-=1
                cows+=1
                v-=1
# 1:1 2:2.     2:1 3:1 1:1
    return str(bulls)+"A"+str(cows)+"B"
    #1222 1234
secret = "1807"
guess =  "7810"
print(getHint(secret, guess))
# # def isBadVersion(version):
# def firstBadVersion(self, n):
#     low,high = 1,n
#     probable_ans = n
#     while low<high:
#         mid = low+(high-low)//2
#         if isBadVersion(mid):
#             high = mid
#             probable_ans = mid
#         else:
#             low = mid+1
#     return probable_ans

# [0, 0, 0, 1, 1, 1]


        