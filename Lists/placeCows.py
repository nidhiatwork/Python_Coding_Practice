'''Farmer has C cows and N stalls. All the C cows must be placed in the N stalls such that the minimum distance between any two of them is as large as possible. Print the largest distance'''
def placeCows(arr, C):
    low = 0
    ans = 0
    high = len(arr)
    while low<=high:
        mid = (low + high)//2
        if canPutCowsWithDist(mid, C, arr):
            low = mid+1
            ans = mid
        else:
            high = mid-1
    return ans

def canPutCowsWithDist(x, C, arr):
    idx=0
    while idx<len(arr):
        C-=1
        if C==0:
            return True
        idx+=x
    return False

arr = [1,2,3,4]
C = 3
print(placeCows(arr, C))