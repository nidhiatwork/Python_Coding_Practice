
''' Find whether you can reach last index
'''

def canJump(arr):
    mx = 0
    for i in range(len(arr)): # i stores index from 0 to n-1
        if i>mx:
            return False
        mx = max(mx, arr[i] + i)
    return True

arr = [2,0,1,1,4]
print(canJump(arr))