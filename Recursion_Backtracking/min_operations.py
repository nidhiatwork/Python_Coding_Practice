# Your solution
def min_operations(target,num=1,op=1):
    if num>target:
        return target+1
    if num==target:
        return op
    add_op = min_operations(target, num+1, op+1)
    double_op = min_operations(target, num*2, op+1)
    return min(add_op, double_op)

# Test Cases

def test_function(test_case):
    target = test_case[0]
    solution = test_case[1]
    output = min_operations(target)
    if output == solution:
        print("Pass")
    else:
        print("Fail")
target = 5
solution = 4
test_case = [target, solution]
test_function(test_case)