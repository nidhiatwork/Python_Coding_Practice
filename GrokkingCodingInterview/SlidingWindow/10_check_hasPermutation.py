from collections import defaultdict
from collections import Counter
def do(s,p):
    frequency = Counter(p)
    window_start,window_end=0,0
    matched=0
    for window_end in range(len(s)):
        if s[window_end] in frequency:
            frequency[s[window_end]]-=1
            if frequency[s[window_end]]==0:
                matched+=1
        if matched==len(frequency):
            return True
        if window_end>=len(p)-1:
            if s[window_start] in frequency:
                if frequency[s[window_start]]==0:
                    matched-=1
                frequency[s[window_start]]+=1
            window_start+=1
    return False
print(do("oidbcaf", "abc"))
