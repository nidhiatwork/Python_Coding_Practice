from collections import Counter
def gridSearch(grid, word):
    coords = []
    p=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if findCoords(grid, word, coords, i, j, p):
                return coords
    return coords

def findCoords(grid, word, coords, i, j, p):
    if word[p]!=grid[i][j]:
        return False
    coords.append((i,j))
    if p==len(word)-1:
        return True
    for dir in ([1,0], [0,1]):
        new_i = i+dir[0]
        new_j = j+dir[1]
        if isSafe(grid, new_i, new_j):
            if findCoords(grid, word, coords, new_i, new_j, p+1):
                return coords 
    coords.pop()
    return False

def isSafe(grid, i, j):
    return i<len(grid) and j<len(grid[0])

grid1 = [
    ['b', 'b', 'b', 'a', 'l', 'l', 'o', 'o'],
    ['b', 'a', 'c', 'c', 'e', 's', 'c', 'n'],
    ['a', 'l', 't', 'e', 'w', 'c', 'e', 'w'],
    ['a', 'l', 'o', 's', 's', 'e', 'c', 'c'],
    ['w', 'o', 'o', 'w', 'a', 'c', 'a', 'w'],
    ['i', 'b', 'w', 'o', 'w', 'w', 'o', 'w'],
]
word1_1 = "access"
word1_2 = "balloon"
word1_3 = "wow"
word1_4 = "sec"

grid2 = [
    ['a'],
]
word2_1 = "a"

grid3 = [
    ['c', 'a'],
    ['t', 't'],
    ['h', 'a'],
    ['a', 'c'],
    ['t', 'g'],
]
word3_1 = "cat"
word3_2 = "hat"

grid4 = [
    ['c', 'c', 'x', 't', 'i', 'b'],
    ['c', 'a', 't', 'n', 'i', 'i'],
    ['a', 'x', 'n', 'x', 'p', 't'],
    ['t', 'x', 'i', 'x', 't', 't'],
]
word4_1 = "catnip"
print(gridSearch(grid1, word1_4))