def secondLargest(arr):
    mx1 = -float("inf")
    mx2 = -float("inf")

    for num in arr:
        if num >mx1:
            mx2= mx1
            mx1=num
        elif num>mx2:
            mx2 = num
    return mx2


arr = [5,2,7,1,3,4,6,8]
print(secondLargest(arr))