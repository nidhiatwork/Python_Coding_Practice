'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
Input: 2, [[1,0],[0,1]]
Output: false
Explanation:  it is impossible.
'''
#To do
def canFinish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    visited = [0]* numCourses
    for x, y in prerequisites:
        graph[x].append(y)
    def hasCycle(v):
        if visited[v] == 1:
            return False
        if visited[v] == -1:
            return True
        visited[v] = -1
        for i in graph[v]:
            if not hasCycle(i):
                return False
        visited[v] = 1
        return False
    for i in range(numCourses):
        if hasCycle(i):
            return False
    return True

print(canFinish(4, [[1,0],[1,3]]))