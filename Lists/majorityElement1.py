'''
Write a function which takes an array and prints the majority element (if it exists), otherwise prints “No Majority Element”. A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element). 
[3,6,3,8,3,2,3,3,6,3]
'''
# Program for finding out majority element in an array

# Function to find the candidate for Majority


def findCandidate(A):
	candidate = A[0]
	count = 0
	for num in A:
		if num==candidate:
			count += 1
		else:
			count -= 1
		if count == 0:
			candidate = num
			count = 1
	return candidate


def isMajority(A, cand):
	count = 0
	for num in A:
		if num == cand:
			count += 1
	return count > len(A)/2

# Function to print Majority Element


def printMajority(A):
	# Find the candidate for Majority
	cand = findCandidate(A)

	# Print the candidate if it is Majority
	if isMajority(A, cand) == True:
		print(cand)
	else:
		print("No Majority Element")


# Driver code
A = [3,6,3,8,3,2,3,3,6,3]

# Function call
printMajority(A)

