
def printNearestPrime(x):
    i=1
    while(True):
        if isPrime(x+i):
            return x+i
        elif isPrime(x-i):
            return x-i
        else:
            x+=1

def isPrime(n):
    isPrime = True
    for i in range(2,(n//2)+1):
        if n%i==0:
            isPrime = False
            break
    return isPrime

x = 1
print(printNearestPrime(x))