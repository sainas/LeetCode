class Solution:
    def queryString(self, S: str, N: int) -> bool:
        if N > int(S,2):
            return False
        for i in range(N):
            mystr = bin(N-i)[2:]
            if not mystr in S:
                return False
        return True