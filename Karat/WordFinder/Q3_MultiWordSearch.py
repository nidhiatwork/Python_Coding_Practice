from collections import Counter
def gridSearch(grid, words):
    mp = []
    for word in words:
        coord = []
        coords = []
        p=0
        findCoordsHelper(grid, word, coord, coords, p)
        mp.append(coords)
    combs=mp[0]
    combs = AllPossiblePaths(mp,combs)
    return distinctPaths(combs)

def distinctPaths(combs):
    for paths in combs:
        if not overlapping(paths):
            return paths
    return []

def overlapping(paths):
    final_set = set()
    for pth in paths:
        for item in pth:
            final_set.add(item)
    return len(final_set)!=len_paths(paths)

def len_paths(paths):
    all_paths=[]
    for pth in paths:
        for item in pth:
            all_paths.append(item)
    return len(all_paths)

def AllPossiblePaths(mp, combs, i=1):
    if i==len(mp):
        return combs
    ans = []
    for comb in combs:
        for path in mp[i]:
            temp=[]
            if isinstance(comb[0], list):
                for item in comb:
                    temp.append(item)
            else:
                temp.append(comb)
            temp.append(path)
            ans.append(temp)
    combs = ans
    return AllPossiblePaths(mp,combs,i+1)

def isValid(mp, i, j):
    return i<len(mp) and j<len(mp[i])


def findCoordsHelper(grid, word, coord, coords, p):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==word[0]:
                coord =[(i,j)]
                findCoords(grid, word, coord, coords, i, j, p+1)

def findCoords(grid, word, coord, coords, i, j, p):
    if p==len(word):
        coords.append(coord.copy())
        return
    for dir in ([1,0], [0,1]):
        new_i = i+dir[0]
        new_j = j+dir[1]
        if isSafe(grid, new_i, new_j, word, p):
            coord.append((new_i, new_j))
            findCoords(grid, word, coord, coords, new_i, new_j, p+1)
            coord.pop()

def isSafe(grid, i, j, word, p):
    return i<len(grid) and j<len(grid[0]) and word[p]==grid[i][j]

grid1 = [
    ['b', 'a', 'b'],
    ['y', 't', 'a'],
    ['x', 'x', 't'],
]
words1_1 = ['by', 'bat']
# words1_1 = ['bat', 'by']

grid2 =[
    ['A', 'B', 'A', 'B'],
    ['B', 'A', 'B', 'A'],
    ['A', 'B', 'Y', 'B'],
    ['B', 'Y', 'A', 'A'],
    ['A', 'B', 'B', 'A'],
]
words2_1 = ['ABABY', 'ABY', 'AAA', 'ABAB', 'BABB']
words2_2 = ['ABABA', 'ABA', 'BAB', 'BABA', 'ABYB']
print(gridSearch(grid1, words1_1))