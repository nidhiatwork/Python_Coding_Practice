# 	1. given array of int, choose different index i,j -> return max val arr[i]-1 * arr[j]-1
# 	[1,3,-2,4,2, -5]
# 	[-3, -1, -5]
# 	[4,7,2,0]

'''
0 neg, 2 pos # DONE
0 neg, 1 pos # base case
0 neg, 0 pos # DONE
1 neg, 2 pos # DONE
1 neg, 1 pos # DONE
1 neg, 0 pos # DONE
2 neg, 2 pos # DONE
2 neg, 1 pos # DONE
2 neg, 0 pos # DONE

'''
def findMaxProduct(arr):
	if len(arr)<2:
		return
	new_arr = []
	posCount, negCount, zeroCount = 0,0,0
	for item in arr:
		new_arr.append(item-1)
		if item>0:
			posCount+=1
		elif item<0:
			negCount+=1
		else:
			zeroCount+=1
	print(new_arr)
	mx1 = -float('inf')
	mx2 = -float('inf')
	nmx1 = float('inf')
	nmx2 = float('inf')
	
	for item in new_arr:
		if item>0:
			if item>mx1:
				mx2 = mx1
				mx1 = item
			elif item>mx2:
				mx2 = item
		if item<=0:
			if item<nmx1:
				nmx2 = nmx1
				nmx1 = item
			elif item<nmx2:
				nmx2 = item
	
	if posCount>=2 and negCount>=2:
		return max(mx1*mx2, nmx1*nmx2)
	elif posCount>=2:
		return mx1 * mx2
	elif negCount>=2:
		return nmx1 * nmx2
	elif posCount==1 and negCount==1 and zeroCount==0:
		return mx1 * nmx1
	else:
		return 0

# arr = [-40, -50,1,3,-2,4,2, -5]
# arr = 	[-3, -1, -5]
arr=	[4,7,2,0]
print(findMaxProduct(arr))
