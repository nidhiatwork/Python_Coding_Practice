'''
For a given array [0...N-1], if arr[i] = j, you have to set arr[j]=i in constant space.
'''

def func_withSpace(arr):
    ans = [None for _ in range(len(arr))]
    for i,item in enumerate(arr):
        ans[item] = i
    return ans

def func2(arr):
    index_to_be_set = arr[0]
    value_to_be_set = 0
    for _ in range(len(arr)):
        tmp = arr[index_to_be_set]
        arr[index_to_be_set] = value_to_be_set
        value_to_be_set = index_to_be_set
        index_to_be_set = tmp
    return arr

arr = [1,0,4,3,2]
print(func2(arr))