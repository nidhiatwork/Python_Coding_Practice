# Given a matrix, zero out every row and column that contains a zero.

import unittest

def zero_out_row_col(m):
    n = len(m) # n X n matrix
    zero_rows, zero_columns = [],[]
    for row in range(n):
        for col in range(n):
            if m[row][col]==0:
                zero_rows.append(row)
                zero_columns.append(col)
                break

    for r in zero_rows:
        for c in range(n):
            m[r][c]=0
    
    for c in zero_columns:
        for r in range(n):
            m[r][c]=0
    

class Test(unittest.TestCase):
    def test_zero_out_row_col_matrix(self):
        mat1 = [[1,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1],[1,1,1,0,1],[2,3,4,5,6]]
        mat2 = [[1,0,1,0,1],[0,0,0,0,0],[1,0,1,0,1],[0,0,0,0,0],[2,0,4,0,6]]
        zero_out_row_col(mat1)
        self.assertEqual(mat1, mat2)

if __name__ == "__main__":
  unittest.main()
