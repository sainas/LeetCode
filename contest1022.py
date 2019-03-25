class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K%2 == 0 or K % 5 ==0:
            return -1
        i = 1
        for lenth in range(1,1000000):
            if i>=K:
                if i%K ==0:
                    return lenth
            i = 10*i + 1
        return -1