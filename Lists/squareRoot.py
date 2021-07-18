def findSqRt(num):
    multiplier = 1
    if num<0:
        multiplier = -1
        num = num*multiplier
    low = 0
    high = (num+1)//2
    probable_ans = None
    while low <= high:
        mid = (low + high)//2
        if mid*mid==num:
            return mid
        elif mid*mid<num:
            low = mid+1
            probable_ans = mid
        else:
            high = mid-1
    return probable_ans * multiplier

for i in range(3):
    if findSqRt(i)!=int(i**0.5):
        print(i)