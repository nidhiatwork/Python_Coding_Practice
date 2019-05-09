
memo={}

def fibo(n):
    print(fib(n))
    print(memo)
def fib(n):
    if n in memo: 
        print("already calculated: ",n)
        return memo[n]
    elif n == 1:
        f = 0
    elif n==2:
        f=1
    else:
        f = fib(n-2) + fib(n-1)
    memo[n] = f
    return f

fibo(7)