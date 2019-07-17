
def operate(a):
    n = len(a)
    rows,cols = 0,0
    while cols<=n-1:
        a[rows][cols]=0
        rows+=1
        cols+=1
    rows,cols=0,n-1
    while cols>=0:
        a[rows][cols]=0
        cols-=1
        rows+=1

a = [[1,2,3],[4,5,6],[7,8,9]]
operate(a)
print(a)