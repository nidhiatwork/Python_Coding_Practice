def find_pairs_brute(l,k):
    ans=[]
    for i in range(len(l)):
	    for j in range(i+1,len(l)):
		    if abs(l[i]-l[j])==k:
			    ans.append((l[i],l[j]))
    return ans

def findPairs(lst, k): 
      
    return [(e1, e2) for e1 in lst  
            for e2 in lst if (e1-e2 == k)] 

def find_Pairs(lst, k): 
    res = [] 
    for e in lst: 
        if e + k in lst: 
            res.append((e, e + k))             
    return res 

def find_pairs_lookup(l,k):
    ans=set()
    for item in l:
        if item+k in l:
            ans.add((item,item+k))
        elif item-k in l:
            ans.add((item-k,item))
    return ans


l = [1, 7, 5, 9, 2, 12, 3]
print(find_Pairs(l,2))