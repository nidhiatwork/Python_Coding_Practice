
def flipAndInvertImage(A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for row in A:
            result.append(list(map(lambda x: 0 if x == 1 else 1, row[::-1])))
        return result



nums = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(flipAndInvertImage(nums))