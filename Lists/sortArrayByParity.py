'''
Separate odds from even in a list.
'''

def sortArrayByParity(A):
    l = 0
    r = len(A) - 1
    while (l < r):
        if (A[l] % 2 != 0):
            A[l], A[r] = A[r],A[l]
            r-=1
        else:
            l+=1
    return A
    
A = [3,1,2,4]
print(sortArrayByParity(A))
