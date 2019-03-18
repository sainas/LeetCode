## 1012. Complement of Base 10 Integer
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        start = 2
        while start<(N+1):
            start *=2
        return start-N-1
        