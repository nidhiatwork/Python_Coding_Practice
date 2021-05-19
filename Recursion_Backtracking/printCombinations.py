'''
Print all combinations of numbers from 1 to `n` having sum `n`
For n = 5, the following combinations are possible:
 
{ 5 }
{ 1, 4 }
{ 2, 3 }
{ 1, 1, 3 }
{ 1, 2, 2 }
{ 1, 1, 1, 2 }
{ 1, 1, 1, 1, 1 }
# '''

def printCombinations(val, n, out): 
	if n == 0:
		print(out)
		return
 
	for v in range(val, n + 1):
		out.append(v)
		printCombinations(v, n - v, out)
		out.pop()

if __name__ == '__main__':
 
	n = 5
	out = []
	printCombinations(1, n, out)
