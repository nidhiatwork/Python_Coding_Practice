def inv_count(arr, ct=0):
    if len(arr)==1:
        return 0
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    ct1 = inv_count(L, ct)
    ct2 = inv_count(R, ct)
    ct+=ct1+ct2
    i=j=k=0
    while i<len(L) and j<len(R):
        if L[i]<=R[j]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
            ct+=(mid-i)
        k+=1
    while i<len(L):
        arr[k]=L[i]
        k+=1
        i+=1
    while j<len(R):
        arr[k]=R[j]
        k+=1
        j+=1
    return ct

arr = [7,6,5]
print(inv_count(arr))