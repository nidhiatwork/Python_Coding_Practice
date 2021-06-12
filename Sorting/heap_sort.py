def heapify_maxOnLeft(arr, i, n):
	largest_index = i 
	left_node = 2 * i + 1     
	right_node = 2 * i + 2     
  
	if left_node < n and arr[i] < arr[left_node]: 
		largest_index = left_node
  
	if right_node < n and arr[largest_index] < arr[right_node]: 
		largest_index = right_node
  
	if largest_index != i: 
		arr[i], arr[largest_index] = arr[largest_index], arr[i] 
	
		heapify_maxOnLeft(arr, largest_index,n) 
		
def heapsort(arr):
	n = len(arr) 

	for i in range(n-1, -1, -1): 
		heapify_maxOnLeft(arr, i,n) 

	for i in range(n-1, -1, -1): 
		arr[i], arr[0] = arr[0], arr[i] 
		heapify_maxOnLeft(arr, 0,i) 

def test_function(test_case):
	heapsort(test_case[0])
	if test_case[0] == test_case[1]:
		print("Pass")
	else:
		print("False")

arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
solution = [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]

test_case = [arr, solution]

test_function(test_case)
