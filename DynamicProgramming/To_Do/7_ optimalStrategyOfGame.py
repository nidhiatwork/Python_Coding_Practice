'''
Consider a row of n coins of values v1 . . . vn, where n is even. We play a game against an opponent by alternating turns. In each turn, a player selects either the first or last coin from the row, removes it from the row permanently, and receives the value of the coin. Determine the maximum possible amount of money we can definitely win if we move first.

5, 3, 7, 10 : The user collects maximum value as 15(10 + 5)

8, 15, 3, 7 : The user collects maximum value as 22(7 + 15)
'''
#recursive way to solve function
def optimalStrategyOfGame(coins,i,j): 
	if j==i:
    		return coins[i]
	elif j==i+1:
    		return max(coins[i],coins[j])
	
	return max(coins[i] + min(optimalStrategyOfGame(coins,i+2,j),optimalStrategyOfGame(coins,i+1,j-1)),coins[j]+min(optimalStrategyOfGame(coins,i+1,j-1),optimalStrategyOfGame(coins,i,j-2)))

# Driver Program to test above function 
coins = [5, 3, 7, 10]
print(optimalStrategyOfGame(coins,0,len(coins)-1))

# A dynamic programming based function 
def dp_optimalStrategyOfGame(arr, n): 
      
    # Create a table to store  
    # solutions of subproblems  
    table = [[0 for i in range(n)] 
                for i in range(n)] 
  
    # Fill table using above recursive  
    # formula. Note that the table is  
    # filled in diagonal fashion  
    # (similar to http://goo.gl/PQqoS), 
    # from diagonal elements to 
    # table[0][n-1] which is the result.  
    for gap in range(n): 
        for j in range(gap, n): 
            i = j - gap 
              
            # Here x is value of F(i+2, j),  
            # y is F(i+1, j-1) and z is  
            # F(i, j-2) in above recursive  
            # formula  
            x = 0
            if((i + 2) <= j): 
                x = table[i + 2][j] 
            y = 0
            if((i + 1) <= (j - 1)): 
                y = table[i + 1][j - 1] 
            z = 0
            if(i <= (j - 2)): 
                z = table[i][j - 2] 
            table[i][j] = max(arr[i] + min(x, y), 
                              arr[j] + min(y, z)) 
    return table[0][n - 1] 
  
# Driver Code 
arr1 = [ 8, 15, 3, 7 ] 
n = len(arr1) 
print(dp_optimalStrategyOfGame(arr1, n)) 
  
arr2 = [ 2, 2, 2, 2 ] 
n = len(arr2) 
print(dp_optimalStrategyOfGame(arr2, n)) 
  
arr3 = [ 20, 30, 2, 2, 2, 10] 
n = len(arr3) 
print(dp_optimalStrategyOfGame(arr3, n))