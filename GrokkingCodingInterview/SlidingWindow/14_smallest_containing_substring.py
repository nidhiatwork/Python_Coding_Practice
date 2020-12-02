from collections import defaultdict
from collections import Counter
import math
def do(s,p):
    freq = Counter(p)
    window_start,window_end=0,0
    matched=0
    min_length=math.inf
    for window_end in range(len(s)):
        if s[window_end] in freq:
            freq[s[window_end]]-=1
            if freq[s[window_end]]>=0:
                matched+=1
        while matched==len(p):
            if min_length> window_end-window_start+1:
                min_length=window_end-window_start+1
                substr = window_start
            if s[window_start] in freq:
                if freq[s[window_start]]==0:
                    matched-=1
                freq[s[window_start]]+=1
            window_start+=1
    if min_length > len(s):
        return ""
    return s[substr:substr+min_length]
            
    
print(do("adcad", "abc"))
