from collections import defaultdict
def do(s,k):
    ws,we=0,0
    l,max_l=0,0
    chars = defaultdict(int)
    for we in range(len(s)):
        chars[s[we]]+=1
        while len(chars)>k:
            if chars[s[ws]]==1:
                del chars[s[ws]]
            else:
                chars[s[ws]]-=1
            ws+=1
        l = we-ws+1
        max_l=max(l,max_l)
    return max_l
        
print(do("cbbebi",3))
