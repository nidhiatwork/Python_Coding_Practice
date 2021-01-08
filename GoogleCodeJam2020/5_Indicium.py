def get_diag_sum(mat):
    return sum([mat[i][i] for i in range(len(mat))])

def getLatinMatrix(combs):
    ans = []
    for i in range(len(combs)):
        combs_copy = [[combs[m][n] for n in range(len(combs[0]))] for m in range(len(combs))]
        m = []
        m.append(combs_copy[i])
        for id,val in enumerate(combs_copy[i]):
            idxs = [k for k in range(len(combs_copy)) if combs_copy[k][id] == val]
            for id in idxs:
                    combs_copy[id] = [0]*len(combs_copy[id])
        for row in combs_copy:
            if any(row):
                m.append(row)
        ans.append(m)
    return ans

def permute_iteration(n):
    nums = [i for i in range(1,n+1)]
    perms = [[]]
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in range(len(perm)+1):
                new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
        perms = new_perms
    return perms    

T = int(input())
t=1
while t<=T:
        possibility = "IMPOSSIBLE"
        inp = input().split(" ")
        N,K = int(inp[0]),int(inp[1])
        combs = permute_iteration(N)
        mats = getLatinMatrix(combs)
        matx = []
        for mat in mats:
            diag_sum = get_diag_sum(mat)
            if diag_sum==K:
                possibility = "POSSIBLE"
                matx = mat
                break
        ans = "Case #"+str(t)+": "+possibility
        print(ans)
        for i in range(len(matx)):
            a= ""
            for j in range(len(matx[0])):
                a+= str(matx[i][j])+ " "
            print(a.strip())
        t+=1