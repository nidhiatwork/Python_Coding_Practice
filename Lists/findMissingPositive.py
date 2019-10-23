'''
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
'''

# Python Program to find the smallest 
# positive missing number 

def firstMissingPositive_1(A):# Our original array 

	m = max(A) # Storing maximum value 
	if m < 1: 
		
		# In case all values in our array are negative 
		return 1
	if len(A) == 1: 
		
		# If it contains only one element 
		return 2 if A[0] == 1 else 1	
	l = [0] * m 
	for i in range(len(A)): 
		if A[i] > 0: 
			if l[A[i] - 1] != 1: 
				
				# Changing the value status at the index of our list 
				l[A[i] - 1] = 1
	for i in range(len(l)): 
		
		# Encountering first 0, i.e, the element with least value 
		if l[i] == 0: 
			return i + 1
			# In case all values are filled between 1 and m 
	return i + 2

def findMissingPositive_2(arr): 
    
    n = len(arr)
    # Default smallest Positive Integer 
    m = 1
  
    # Store values in set which are 
    # greater than variable m 
    x = [] 
    for i in range(n): 
          
        # Store value when m is less than 
        # current index of given array 
        if (m < arr[i]): 
            x.append(arr[i]) 
      
        elif (m == arr[i]): 
              
            # Increment m when it is equal 
            # to current element 
            m = m + 1
  
            while (x.count(m)): 
                x.remove(m) 
  
                # Increment m when it is one of the 
                # element of the set 
                m = m + 1
  
    # Return the required answer 
    return m 

def findMissingPositive_3(array):
    # Pass 1, move every value to the position of its value
    N = len(array)
    if N==0: return 1
    if N==1: return 2 if array[0]==1 else 1

    for cursor in range(N):
        target = array[cursor]
        while target < N and array[target]>=0 and target != array[target]:
            new_target = array[target]
            array[target] = target
            target = new_target

    # Pass 2, find first location where the index doesn't match the value
    for cursor in range(1,N):
        if array[cursor] != cursor:
            return cursor
    return N  

def findMissingPositive_4(nums):
    if not nums:
        return 1
    n = len(nums)
    # 1. mark numbers (num < 0) and (num > n) with a special marker number (n+1) 
    # (we can ignore those because if all number are > n then we'll simply return 1)
    for i in range(n):
        if (nums[i] <= 0 or nums[i] > n) :
            nums[i] = n + 1
    
    #note: all number in the array are now positive, and on the range 1..n+1
    # 2. mark each cell appearing in the array, by converting the index for that number to negative
    for i in range(n):
        num = abs(nums[i])
        if (num > n): 
            continue
        num-=1 
        if (nums[num] > 0) :
            nums[num] = -1 * nums[num]
    
    #3. find the first cell which isn't negative (doesn't appear in the array)
    for i in range(n):
        if (nums[i] >= 0) :
            return i + 1
    #4. no positive numbers were found, which means the array contains all numbers 1..n
    return n + 1

A = [2,1]
print(findMissingPositive_3(A)) 

