'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
def generate_1(numRows):
    ans=dict()
    final_list=[]
    for i in range(1,numRows+1):
        if i==1:
            ans[i]=[1]
        else:
            ans[i]=build(ans[i-1])
    
    for v in ans.values():
        final_list.append(v)
    
    return final_list

def build(l):
    ans=[1]
    for i in range(0,len(l)-1):
        ans.append(l[i]+l[i+1])
    ans.append(1)
    return ans

def generate_2(num_rows):
    triangle = []

    for row_num in range(num_rows):
        # The first and last row elements are always 1.
        row = [None for _ in range(row_num+1)]
        row[0], row[-1] = 1, 1

        # Each triangle element is equal to the sum of the elements
        # above-and-to-the-left and above-and-to-the-right.
        for j in range(1, len(row)-1):
            row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

        triangle.append(row)

    return triangle

print(generate_2(5))