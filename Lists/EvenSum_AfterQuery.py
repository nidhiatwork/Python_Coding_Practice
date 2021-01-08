'''
For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A.
(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)
Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.

'''
# Instead of trying to find sum every time from beginning of array. Lets modify sum for only query index
def sumEvenAfterQueries(A, q):
        ans = []
        S = sum([e for e in A if not e%2])
        for x,k in queries:
            if A[k] % 2 == 0: 
                S -= A[k]
            A[k] += x
            if A[k] % 2 == 0: 
                S += A[k]
            ans.append(S)
        return ans
A = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]
print(sumEvenAfterQueries(A, queries))
