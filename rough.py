

def fib(n):
    first = -1
    second = 1
    for i in range(0,n+1):
        third = first + second
        first = second
        second = third
        print(second)
    return second

fib(8)