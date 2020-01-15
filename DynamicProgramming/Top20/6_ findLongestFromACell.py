'''
Given a n*n matrix where all numbers are distinct, find the maximum length path (starting from any cell) such that all cells along the path are in increasing order with a difference of 1.

We can move in 4 directions from a given cell (i, j), i.e., we can move to (i+1, j) or (i, j+1) or (i-1, j) or (i, j-1) with the condition that the adjacent cells have a difference of 1.

Input:  mat[][] = {{1, 2, 9}
                   {5, 3, 8}
                   {4, 6, 7}}
Output: 4
The longest path is 6-7-8-9. 
We calculate longest path beginning with every cell. Once we have computed longest for all cells, we return maximum of all longest paths
'''

# A dynamic programming based function 
n = 3
# Returns length of the longest path beginning with mat[i][j].  
# This function mainly uses lookup table dp[n][n]  
def findLongestFromACell(i, j, mat, dp): 
    # Base case  
    if (i<0 or i>= n or j<0 or j>= n): 
        return 0
  
    # If this subproblem is already solved  
    if (dp[i][j] != -1):  
        return dp[i][j] 
  
    # To store the path lengths in all the four directions 
    x, y, z, w = -1, -1, -1, -1
  
    # Since all numbers are unique and in range from 1 to n * n,  
    # there is atmost one possible direction from any cell  
    if (j<n-1 and ((mat[i][j] +1) == mat[i][j + 1])): 
        x = 1 + findLongestFromACell(i, j + 1, mat, dp) 
  
    if (j>0 and (mat[i][j] +1 == mat[i][j-1])):  
        y = 1 + findLongestFromACell(i, j-1, mat, dp) 
  
    if (i>0 and (mat[i][j] +1 == mat[i-1][j])): 
        z = 1 + findLongestFromACell(i-1, j, mat, dp) 
  
    if (i<n-1 and (mat[i][j] +1 == mat[i + 1][j])): 
        w = 1 + findLongestFromACell(i + 1, j, mat, dp) 
  
    # If none of the adjacent fours is one greater we will take 1 
    # otherwise we will pick maximum from all the four directions 
    dp[i][j] = max(x, max(y, max(z, max(w, 1)))) 
    return dp[i][j] 
  
  
# Returns length of the longest path beginning with any cell  
def findLongestOverAll(mat): 
    result = 1 # Initialize result  
  
    # Create a lookup table and fill all entries in it as -1  
    dp =[[-1 for i in range(n)]for i in range(n)] 
  
    # Compute longest path beginning from all cells  
    for i in range(n): 
        for j in range(n): 
            if (dp[i][j] == -1): 
                findLongestFromACell(i, j, mat, dp) 
            # Update result if needed  
            result = max(result, dp[i][j])
    return result 
  
# Driver program  
mat = [[1, 2, 9],  
    [5, 3, 8], 
    [4, 6, 7]]  
print("Length of the longest path is ", findLongestOverAll(mat)) 