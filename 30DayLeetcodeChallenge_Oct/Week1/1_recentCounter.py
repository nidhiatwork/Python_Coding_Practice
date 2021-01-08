import collections
class RecentCounter:
    
    def __init__(self):
        self.q = collections.deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while True:
            if not (self.q[0]<=t and self.q[0]>=t-3000):
                self.q.popleft()
            else:
                return len(self.q)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)