'''
Given an integer array arr, count element x such that x + 1 is also in arr.

If there're duplicates in arr, count them seperately.

 

Example 1:

Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
'''

def countElements(arr):
    seen = set()
    for item in arr:
        if item not in seen:
            seen.add(item)
    
    result = 0
    for item in arr:
        if item+1 in seen:
            result+=1
    return result


arr = [1,3,2,3,5,0]
print(countElements(arr))