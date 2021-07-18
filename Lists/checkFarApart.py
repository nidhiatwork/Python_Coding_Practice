'''	Given an array of numbers (0 and 1 only) and an integer k, return true if all 1s are atleast k places away from each other. otherwise FALSE.
	100101101 k=2
'''
def checkFarApart(arr,k):
    lastOneIdx = None
    for i in range(len(arr)):
        if arr[i]==1:
            if not lastOneIdx:
                lastOneIdx = i
            else:
                if i-lastOneIdx<k:
                    return False
                lastOneIdx = i
    return True
