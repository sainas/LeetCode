class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        def sink(i, j):
            if 0 <= i < len(A) and 0 <= j < len(A[0]) and A[i][j] == 1:
                A[i][j] = 0
                list(map(sink, [i+1, i-1, i, i], [j, j, j+1, j-1]))
                return 1
            return 0
        for i in range(len(A)):
            sink(i,0)
            sink(i,len(A[0])-1)
        for j in range(len(A[0])):
            sink(0,j)
            sink(len(A)-1,j)
        return sum(A[i][j] for i in range(len(A)) for j in range(len(A[0])))
    