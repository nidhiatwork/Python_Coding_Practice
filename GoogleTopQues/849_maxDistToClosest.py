'''
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.
Input: [1,0,0,0,1,0,1]
Output: 2
'''

def maxDistToClosest(seats):
    one_indxs = [i for i in range(len(seats)) if seats[i]==1]
    mx=1
    for i in range(1,len(one_indxs)):
        mx = max(mx,(one_indxs[i]-one_indxs[i-1])//2)
    return max(mx,one_indxs[0],len(seats)-1-one_indxs[-1])           

seats = [0,0,0,0,1,0,1,0,0]
print(maxDistToClosest(seats))
