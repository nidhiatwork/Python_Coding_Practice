'''
Write a function int fib(int n) that returns Fn. For example, if n = 0, then fib() should return 0. If n = 1, then it should return 1. For n > 1, it should return Fn-1 + Fn-2

For n = 9
Output:34'''

# Via recursion
def recursion_Fibonacci(n):
    if n<0:
        print("Incorrect input")
    elif n==0 or n == 1:
        return n
    else:
        return recursion_Fibonacci(n-1)+recursion_Fibonacci(n-2)

# print(recursion_Fibonacci(7))

#Via DP
def dp_Fibonacci(n):
    fib=[0,1]
    for i in range(2,n+1):
        fib.append(fib[i-1]+fib[i-2])
    return fib[n]

print(dp_Fibonacci(7))

#Via DP with space optimised
def dp_spaceOptimized_Fibonacci(n):
    if n<0:
        print("Incorrect input")
    first = -1
    second = 1
    for _ in range(0,n+1):
        third = first + second
        first = second
        second = third
    return second

# print(dp_spaceOptimized_Fibonacci(5))
