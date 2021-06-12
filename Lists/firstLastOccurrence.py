'''
find first and last occurrence of an element in a sorted array
'''
def first_and_last_index(arr, number):
    start_index, end_index = 0, len(arr)-1
    index = find_index(arr, number, start_index, end_index)
    if index==-1:
        return [-1,-1]
    first_index, current_index = None, index
    while current_index!=-1:
        first_index = current_index
        current_index = find_index(arr, number, start_index, current_index-1)
    
    last_index, current_index = None, index
    while current_index!=-1:
        last_index = current_index
        current_index = find_index(arr, number, current_index+1, end_index)

    return [first_index,last_index]
    
def find_index(arr, number, start_index, end_index):
    if start_index>end_index:
        return -1
    mid = (start_index+end_index)//2
    if arr[mid]==number:
        return mid
    if arr[mid]<number:
        return find_index(arr, number, mid+1, end_index)
    return find_index(arr, number, start_index, mid-1)

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, number)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

input_list = [1]
number = 1
solution = [0, 0]
test_case_1 = [input_list, number, solution]
test_function(test_case_1)