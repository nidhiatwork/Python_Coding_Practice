'''
A happy string is a string that consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
Valid: "abc", "ac", "b" and "abcbabcbcb" 
Invalid: "aa", "baa" and "ababbc"

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.
 '''
import collections

def getHappyString(n: int, k: int) -> str:
    nextValues = {'a':'bc','b':'ac', 'c':'ab'}
    q = collections.deque(['a','b','c'])
    while len(q[0])!=n:
        prefix = q.popleft()
        for nextVal in nextValues[prefix[-1]]:
            postfix = prefix+nextVal
            q.append(postfix)
        print(q)
    return q[k-1] if k<=len(q) else ''

n,k=3,9
print(getHappyString(n,k))