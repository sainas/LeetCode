class Solution:
    def clumsy(self, N: int) -> int:
        result = 0
        n = N
        while(N>0):
            minus = 0
            if N == n:
                minus = 1
            if N >=4:
                result -= int(N*(N-1)/(N-2))-(N-3)
                N = N-4
            elif N ==3:
                result -=int( N*(N-1)/(N-2))
                N = N-3
            elif N ==2:
                result -= N*(N-1)
                N=N-2
            elif N ==1:
                result -= N
                N=N-1 
            result = result*(-1)*minus
        return result 

## Recursion
class Solution:
    def clumsy(self, N: int) -> int:
        def caltail(n):
            if n == 1: return -1
            if n == 2: return -2
            if n == 3: return -6
            if n == 4: return -5
            return caltail(n - 4) - n * (n - 1) // (n - 2) + (n - 3)
        
        if N == 1: return 1
        if N == 2: return 2
        if N == 3: return 6
        if N == 4: return 7
        return N * (N - 1) // (N - 2) + N - 3 + caltail(N - 4)
## Test             
S=Solution()
print(S.clumsy(10))