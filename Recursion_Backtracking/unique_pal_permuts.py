from collections import Counter
def generatePalindromes(s):
    ans = []
    n = len(s)
    counter = Counter(s)
    odd = [key for key, value in counter.items() if value % 2 != 0]
    if len(odd) > 1:
        return []
    if len(odd) == 1:
        counter[odd[0]] -= 1
        helper(n, odd[0], ans, counter)
    else:
        helper(n, '', ans, counter)
    return ans

def helper(n, sub, ans, counter):
    if len(sub) == n:
        ans.append(sub)
        return 
    for k, v in counter.items():
        if v > 0:
            counter[k] -= 2
            helper(n, k + sub + k, ans, counter)
            counter[k] += 2

s = "aabb"
print(generatePalindromes(s))
