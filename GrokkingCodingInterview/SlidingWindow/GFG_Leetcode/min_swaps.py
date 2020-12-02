'''
iven a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.
Input: data = [1,0,1,0,1]
Output: 1

Ans: find total ones, and find the window of that length having maximum ones. answer would be ones - max

'''


def do(data):
    ones = sum(data)
    cnt_one = max_one = 0
    left = right = 0
    while right < len(data):
        # updating the number of 1's by adding the new element
        cnt_one += data[right]
        right += 1
        # maintain the length of the window to ones
        if right - left > ones:
            # updating the number of 1's by removing the oldest element
            cnt_one -= data[left]
            left += 1
        # record the maximum number of 1's in the window
        max_one = max(max_one, cnt_one)
    return ones - max_one

print(do([1,0,1,0,1,0,0,1,1,0,1]))
                          