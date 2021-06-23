def trap(arr):
    leftToRight, rightToLeft, left, right, water = [], [], 0, 0, 0
    for h in arr:
        left = max(left, h)
        leftToRight.append(left)
    for h in reversed(arr):
        right = max(right, h)
        rightToLeft.append(right)
    rightToLeft.reverse()
    for i in range(len(arr)):
        water += min(leftToRight[i], rightToLeft[i]) - arr[i]
    return water

arr = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(arr))