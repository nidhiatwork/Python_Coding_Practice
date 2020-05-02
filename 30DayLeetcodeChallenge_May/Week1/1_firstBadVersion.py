'''
Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 
'''
def firstBadVersion(n):
    low = 1
    high = n
    while low<high:
        mid = low + (high-low)//2
        if isBadVersion(mid):
            high = mid
        else:
            low = mid+1
    return low

def isBadVersion(n):
    return n>=5

n = 5
print(firstBadVersion(n))