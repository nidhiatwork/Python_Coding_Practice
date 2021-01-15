'''We are given an array containing positive and negative numbers. Suppose the array contains a number ‘M’ at a particular index. Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative move backwards ‘M’ indices. You should assume that the array is circular which means two things:

If, while moving forward, we reach the end of the array, we will jump to the first element to continue the movement.
If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the movement.
Write a method to determine if the array has a cycle.'''

from collections import Counter
def circular_array_loop_exists(arr):
    for i in range(len(arr)):
        is_forward = arr[i]>=0
        slow,fast=i,i
        while True:
            slow = find_next_idx(arr, is_forward, slow)
            fast = find_next_idx(arr, is_forward, fast)
            if fast!=-1:
                fast = find_next_idx(arr, is_forward, fast)
            if slow==-1 or fast==-1 or slow==fast:
                break
        if slow!=-1 and slow==fast:
            return True
    return False

def find_next_idx(arr, is_forward,i):
    cur_direction = arr[i]>=0
    if cur_direction!=is_forward:
        return -1
    next_idx = (i + arr[i])%len(arr)
    if i==next_idx:
        return -1
    return next_idx


arr = [1,2,-1,2,2]
print(circular_array_loop_exists(arr))