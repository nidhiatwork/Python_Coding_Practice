from collections import defaultdict

class Solution(object):
    def accountsMerge(self, accounts):
        visited_accounts = [False] * len(accounts)
        emails_accounts_map = defaultdict(list)
        res = []
        # Build up the graph.
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                emails_accounts_map[email].append(i)
        
        # Perform DFS for accounts and add to results.
        for i, account in enumerate(accounts):
            if not visited_accounts[i]:
	            name, emails = account[0], set()
	            self.dfs(i, emails, visited_accounts, accounts, emails_accounts_map)
	            res.append([name] + sorted(emails))
        return res
        
    # DFS code for traversing accounts.
    def dfs(self, i, emails, visited_accounts, accounts, emails_accounts_map):
        if visited_accounts[i]:
            return
        visited_accounts[i] = True
        for email in accounts[i][1:]:
            emails.add(email)
            for neighbor in emails_accounts_map[email]:
                self.dfs(neighbor, emails, visited_accounts, accounts, emails_accounts_map)

# accounts = \
# [["John","johnsmith@mail.com","john_newyork@mail.com"],
# ["John","johnsmith@mail.com", "john00@mail.com"],
# ["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

accounts = \
[["n1","e1","e2"],
["n1","e1", "e3"],
["n2","e4"],
["n3","e5"]]
s = Solution()
print(s.accountsMerge(accounts))