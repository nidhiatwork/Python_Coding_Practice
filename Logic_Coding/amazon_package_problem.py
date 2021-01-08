import sys
def IDsOfPackages(truckSpace, packagesSpace):
    space = truckSpace-30
    i,j=0,len(packagesSpace)-1
    min= sys.maxint
    while(i<j):
        sum = packagesSpace[i]+packagesSpace[j]
        if sum>space:
            j-=1
        else:
            diff = space-sum
            if diff<min:
                min=diff
                trucks=[packagesSpace[i], packagesSpace[j]]
            i+=1
    ans=[]
    for i in trucks:
        if i in d.keys():
            ans.append(d[i])
    return ans
    

a=[210,30]
print(IDsOfPackages(110,a))