from collections import defaultdict
def do(fruits):
    wwindow_start,window_end=0,0
    l,max_l=0,0
    mp=defaultdict(int)
    for window_end in range(len(fruits)):
        mp[fruits[window_end]]+=1
        while len(mp)>2:
            if mp[fruits[wwindow_start]]==1:
                del mp[fruits[wwindow_start]]
            else:
                mp[fruits[wwindow_start]]-=1
            wwindow_start+=1
        l=window_end-wwindow_start+1
        max_l=max(l,max_l)
    return max_l

print(do(["A", "B", "C", "A", "C"]))
