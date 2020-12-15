from collections import defaultdict
from collections import Counter

def checkPerm(s1,s2):
    frequency = Counter(s1)
    window_start,window_end=0,0
    matched=0
    for window_end in range(len(s2)):
        if s2[window_end] in frequency:
            frequency[s2[window_end]]-=1
            if frequency[s2[window_end]]==0:
                matched+=1
        if matched==len(frequency):
            return True
        if window_end>=len(s1)-1:
            if s2[window_start] in frequency:
                if frequency[s2[window_start]]==0:
                    matched-=1
                frequency[s2[window_start]]+=1
            window_start+=1
    return False

print(checkPerm("abc","oaaidbcaf"))
