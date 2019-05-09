"""
# Given a matrix, zero out every row and column that contains a zero.

"""

def operate(s1,s2):
    if len(s1)!=len(s2):
        return False
    
    for i in range(len(s2)):
        if s1[0]==s2[i]:
            for j in range(len(s2)):
                idx = (j+i)%len(s2)
                if s1[j]!=s2[idx]:
                    return False
            return True
    return False

print(operate("nidhi", "inidh"))