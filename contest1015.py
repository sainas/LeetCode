## From discussion
## https://leetcode.com/problems/numbers-with-1-repeated-digit/discuss/256793/Python-DFS-TLE

class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        self.count = 0
        def dfs(n, mask):
            if n > N: return
            print(n)
            self.count += 1
            for i in range(10):
                if not (mask & (1<<i)): 
                    dfs(n*10+i, mask|(1<<i))
        for i in range(1,10):
            dfs(i, 1 << i)
        return N - self.count

## https://leetcode.com/problems/numbers-with-1-repeated-digit/discuss/256725/JavaPython-Count-the-Number-Without-Repeated-Digit
# def numDupDigitsAtMostN(self, N):
#         L, res, n = map(int, str(N + 1))
#         res, n = 0, len(L)

#         def A(m, n):
#             return 1 if n == 0 else A(m, n - 1) * (m - n + 1)

#         for i in range(1, n): res += 9 * A(9, i - 1)
#         s = set()
#         for i, x in enumerate(L):
#             for y in range(0 if i else 1, x):
#                 if y not in s:
#                     res += A(9 - i, n - i - 1)
#             if x in s: break
#             s.add(x)
#         return N - res


s=Solution()
print(s.numDupDigitsAtMostN(100))