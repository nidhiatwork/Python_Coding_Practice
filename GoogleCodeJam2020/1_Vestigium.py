def find_diag_sum(mat):
    return sum([int(mat[i][i]) for i in range(len(mat))]) #store diagonal elements and return sum

def getFaultyRows(mat):
    faulty_rows = 0
    for row in mat:
        if len(set(row))!=len(row):
            faulty_rows+=1
    return faulty_rows

def getFaultyCols(mat):
    faulty_cols = 0
    for col in zip(*mat):
        if len(set(col))!=len(col):
            faulty_cols+=1
    return faulty_cols

T = int(input())
t=1
while t<=T:
    N = int(input())
    mat = []
    for i in range(N):
        inp = input().split(" ")
        mat.append(inp)
    diagonal_sum = find_diag_sum(mat)
    faulty_rows = getFaultyRows(mat)
    faulty_cols = getFaultyCols(mat)
    ans = "Case #"+str(t)+": "+str(diagonal_sum)+" "+str(faulty_rows)+" "+str(faulty_cols)
    print(ans)
    t+=1
