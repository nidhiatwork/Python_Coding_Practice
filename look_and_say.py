#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'lookAndSayQueries' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY q as parameter.
#

def lookAndSayQueries(q):

    ans=[]
    for n in q:  
        s = "11"
        if (n == 1): 
            s= "1"
        if (n == 2): 
            s= "11" 
        for i in range(3, n + 1): 
            s += '$'
            l = len(s)
            cnt = 1 
            tmp = ""      
            for j in range(1 , l):                
                if (s[j] != s[j - 1]):                    
                    tmp += str(cnt + 0)   
                    tmp += s[j - 1]    
                    cnt = 1                
                else: 
                    cnt += 1  
            s = tmp
        ans.append(s)    
    return ans

if __name__ == '__main__':
    q=[1,2,3,4]
    result = lookAndSayQueries(q)
    print(result)