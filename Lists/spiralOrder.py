'''
Given matrix matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

'''

def spiralOrder(matrix):
    
    """ 
    t: top of the matrix
    b: botom of the matrix
    l: left of the matrix
    r: Right of yhe matrix
    dr: printing direction
    m: Number of rows in the matrix
    n: Number of Columns in the matrix
    
    """
    ans = []
    m = len(matrix)
    n = len(matrix[0])
    
    t = 0
    b = m-1
    l = 0
    r = n - 1
    dr = 0
    
    
    while (t <= b and l <=r):
        
        if dr ==0:
            for i in range(l,r+1):
                ans.append(matrix[t][i])
            t +=1
            dr = 1
            
        elif dr ==1:
            for i in range(t,b+1):
                ans.append(matrix[i][r])
            r -=1 
            dr = 2
            
        elif dr ==2:
            for i in range(r,l-1,-1):
                ans.append(matrix[b][i])
            b -=1
            dr = 3
            
        elif dr ==3:
            for i in range(b,t-1,-1):
                ans.append(matrix[i][l])
            l +=1
            dr = 0
    return ans


matrix = [
    [1,2,3,4,5,6,7],
    [8,9,10,11,12,13,14],
    [15,16,17,18,19,20,21],
    [22,23,24,25,26,27,28],
    [29,30,31,32,33,34,35],
    [36,37,38,39,40,41,42],
    [43,44,45,46,47,48,49]
    ]
print(spiralOrder(matrix))