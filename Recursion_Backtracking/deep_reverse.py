''' 
Define a procedure, deep_reverse, that takes as input a list, and returns a new list that is the deep reverse of the input list.
This means it reverses all the elements in the list, and if any of those elements are lists themselves, reverses all the elements in the inner list, all the way down.

Note: The procedure must not change the input list itself.

Example
Input: [1, 2, [3, 4, 5], 4, 5]
Output: [5, 4, [5, 4, 3], 2, 1]
'''
def deep_reverse_2(arr):
    if len(arr)<1:
        return arr
    ans = []
    for item in reversed(arr):
        if type(item) is list:
            item = deep_reverse(item)
        ans.append(item)
    return ans
    
def deep_reverse(arr):
    ans = []
    index = len(arr)-1
    return deep_reverse_helper(arr, index, ans)

def deep_reverse_helper(arr, index, ans):
    if index<0:
        return ans
    item_to_append = arr[index]
    if isinstance(item_to_append,list):
        idx = len(item_to_append)-1
        items = []
        item_to_append = deep_reverse_helper(item_to_append, idx, items)
    ans.append(item_to_append)
    return deep_reverse_helper(arr, index-1, ans)


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = deep_reverse(arr)
    if output == solution:
        print("Pass")
    else:
        print("False")

arr = [1, 2, [3, 4, 5], 4, 5]
solution = [5, 4, [5, 4, 3], 2, 1]
test_case = [arr, solution]
test_function(test_case)