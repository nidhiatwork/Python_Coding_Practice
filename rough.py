'''

'''

def do_Sum(n):
    if n==0:
        return 0
    return n%10 + do_Sum(n//10)

n = 632415
print(do_Sum(n))

