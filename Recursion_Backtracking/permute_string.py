import copy
def permutations(string):
    """
    :param: input string
    Return - list of all permutations of the input string
    TODO: complete this function to return a list of all permutations of the string
    """
    index = 0
    perms = [""]
    return permutations_helper(string,index,perms)

def permutations_helper(string, index, perms):
    if index==len(string):
        return perms
    ans = []
    for perm in perms:
        for i in range(len(perm)+1):
            combination = perm[:i] + string[index] + perm[i:]
            ans.append(combination)
    perms = copy.deepcopy(ans)
    return permutations_helper(string, index+1, perms)
    
def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")

string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test_function(test_case)