
def subsetsWithSum_helper(arr, sum, i, subs):
    if sum==0:
        print(subs)
        return
    elif sum<0 or i<0:
        return
    subsetsWithSum_helper(arr, sum, i-1, subs)
    subs.append(arr[i-1])
    subsetsWithSum_helper(arr, sum-arr[i-1], i-1, subs)
    subs.pop()

def subsetsWithSum(arr, sum):
    subs = []
    n = len(arr)-1
    subsetsWithSum_helper(arr, sum, n, subs)

arr = [2, 3, 5, 6, 8, 10]
sum = 10
subsetsWithSum(arr, sum)