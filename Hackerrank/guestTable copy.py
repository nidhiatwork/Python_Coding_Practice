def guestTable(generosities):
    #
    # Write your code here.
    #
    generosities.sort(key=lambda x:-sum(x))
    print(generosities)
#
# Complete the solve function below.
#
def solve():
    #
    # Write your code here.
    #
    for generosity in generosities:
        if len(generosity) > len(charms[0]*k):
            return -1
    charms.sort(key=lambda x:-sum(x))
    charity = 0
    for r in range(t):
        i,j=0,0
        while i<len(charms[0]) and j<len(generosities[r]):
            charity+= charms[0][i]*generosity[r][j]
            i-=1
            j-=1
    return charity       

        


if __name__ == '__main__':
    
