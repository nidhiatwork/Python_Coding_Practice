'''
find median in an array which is row and column wise sorted.
'''
def binaryMedian(m, r, c):
	mi = m[0][0]
	mx = 0
	for row in m:
		if row[0]<mi:
			mi = row[0]
		if row[-1]>mx:
			mx=row[-1]	
	
	desired = (r * c + 1) // 2
	
	while (mi < mx):
		mid = mi + (mx - mi) // 2
		count_lessThanMid = 0
		for row in m:
			count_lessThanMid+= sum([1 for item in row if item<=mid])
		if count_lessThanMid < desired:
			mi = mid + 1
		else:
			mx = mid
	return mi
	
# Driver code
r, c = 3, 3

m = [ [1, 3, 5], [2, 6, 9], [3, 6, 9]]
print(binaryMedian(m, r, c))

# This code is contributed by Sachin BIsht
