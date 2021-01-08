'''
Do jump search
'''
import math
def jump_search(arr,x):
    step = int(math.sqrt(len(arr)))
    prev,next = 0,step
    while next<len(arr) and (arr[next])<=x:
        prev = next
        next+=step
        
    for i in range(prev,min(next+1,len(arr))):
        if arr[i]==x:
            return i
    return -1



arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 
    34, 55, 89, 144, 233, 377, 610 ]
print(jump_search(arr, 377))

