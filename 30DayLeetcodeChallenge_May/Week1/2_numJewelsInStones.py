
def numJewelsInStones(J,S):
    count = 0
    for s in S:
        if s in J:
            count+=1
    return count

J,S = "aA", "aAAbbbb"
print(numJewelsInStones(J,S))