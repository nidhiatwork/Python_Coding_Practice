'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
'''

def checkStraightLine(coordinates):
    if coordinates[1][0]==coordinates[0][0]:
        for i in range(2,len(coordinates)):
            if (coordinates[i][0]!=coordinates[i-1][0]):
                return False
        return True
    slope = (coordinates[1][1]-coordinates[0][1])//(coordinates[1][0]-coordinates[0][0])
    for i in range(2,len(coordinates)):
        if coordinates[i][0]==coordinates[i-1][0]:
            return False
        if (coordinates[i][1]-coordinates[i-1][1])//(coordinates[i][0]-coordinates[i-1][0])!=slope:
            return False
    return True


coordinates = [[-3,-2],[-1,-2],[2,-2],[-2,-2],[0,-2]]
print(checkStraightLine(coordinates))