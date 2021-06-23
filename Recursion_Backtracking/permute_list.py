'''
Print all permutations of a list 
'''
import copy

def permute(inputList):
    """
    Args: myList: list of items to be permuted
    Returns: list of permutation with each permuted item being represented by a list
    """
    index = 0
    compoundList = [[]]
    return permute_helper(inputList, index, compoundList)

def permute_helper(inputList, index, compoundList):
    if index==len(inputList):
        return compoundList
    ans = []
    for l in compoundList:
        for i in range(len(l)+1):
            combination = l[:i] + [inputList[index]] + l[i:]
            ans.append(combination)
    compoundList = copy.deepcopy(ans)
    return permute_helper(inputList, index+1, compoundList)
# Test Cases 

# Helper Function
def check_output(output, expected_output):
    """
    Return True if output and expected_output
    contains the same lists, False otherwise.
    
    Note that the ordering of the list is not important.
    
    Examples:
        check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

    Args:
        output(list): list of list
        expected_output(list): list of list
    
    Returns:
        bool
    """
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input
    
    o.sort()
    e.sort()
    return o == e

# print ("Pass" if  (check_output(permute([]), [[]])) else "Fail")
# print ("Pass" if  (check_output(permute([0]), [[0]])) else "Fail")
# print ("Pass" if  (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
print ("Pass" if  (check_output(permute([0, 1, 2]), [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])) else "Fail")
a=2