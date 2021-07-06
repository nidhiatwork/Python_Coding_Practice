import collections
class Solution:
	def numOfMinutes(self, n, headID, manager, informTime):
		g = collections.defaultdict(list)
		for i in range(n):
			if manager[i]!=-1:
				g[manager[i]].append(i)
		q = collections.deque()
		q.append((headID,0))
		res = 0
		while q:
			m,t = q.popleft()
			res = max(res, t)
			for emp in g[m]:
				timeElapsed = t + informTime[m]
				q.append((emp, timeElapsed))
		return res
s = Solution()
# n =8
# headID = 0
# manager = [-1,5,0,6,7,0,0,0]
# informTime = [89,0,0,0,0,523,241,519]
n = 15
headID = 0
manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
informTime = [1,1,4,4,1,1,1,0,0,0,0,0,0,0,0]
print(s.numOfMinutes(n, headID, manager, informTime))
