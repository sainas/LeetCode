class Solution:
    def largestSumAfterKNegations(self, A, K: int) -> int:
        import heapq
        summinu = 0
        for i in A:
            if i < 0:
                summinu +=1
        if K >= summinu:
            if (K-summinu)%2==0:
                return sum(map(abs,A))
            else:
                return sum(map(abs,A))-2*min(map(abs,A))
        else:
        #     return sum(abs(A))-2*min(A)
            return sum(A)-2*sum(list(heapq.nsmallest(K, A)))

