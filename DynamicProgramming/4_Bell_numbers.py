'''
Given a set of n elements, find number of ways of partitioning it.
Input:  n = 2
Output: Number of ways = 2
Explanation: Let the set be {1, 2}
            { {1}, {2} } 
            { {1, 2} }
Input:  n = 3
Output: Number of ways = 5
Explanation: Let the set be {1, 2, 3}
             { {1}, {2}, {3} }
             { {1}, {2, 3} }
             { {2}, {1, 3} }
             { {3}, {1, 2} }
             { {1, 2, 3} }

What is a Bell Number?
Let S(n, k) be total number of partitions of n elements into k sets. The value of n’th Bell Number is sum of S(n, k) for k = 1 to n.
Value of S(n, k) can be defined recursively as, S(n+1, k) = k*S(n, k) + S(n, k-1)
1
1 2
2 3 5
5 7 10 15
15 20 27 37 52
Thats why, Bell(3) = 5
'''

def bellNumber(n): 
	Bell = [[0 for i in range(n+1)] for j in range(n+1)]
	Bell[0][0] = 1
	for i in range(1,n+1):
		Bell[i][0] = Bell[i-1][i-1]
		for j in range(1,i+1):
			Bell[i][j] = Bell[i-1][j-1] + Bell[i][j-1]
	return Bell[n][0]

# Driver program 
for n in range(6): 
    print('Bell Number', n, 'is', bellNumber(n)) 