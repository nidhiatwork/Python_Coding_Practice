from collections import defaultdict
def do(s,k):
    window_start,window_end=0,0
    l,max_l=0,0
    chars = defaultdict(int)
    for window_end in range(len(s)):
        chars[s[window_end]]+=1
        while len(chars)>k:
            if chars[s[window_start]]==1:
                del chars[s[window_start]]
            else:
                chars[s[window_start]]-=1
            window_start+=1
        l = window_end-window_start+1
        max_l=max(l,max_l)
    return max_l
        
print(do("cbbebi",3))
