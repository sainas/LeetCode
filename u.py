class Solution:
    def maxScoreSightseeingPair(self, A) -> int:
        maxi=A[0]+A[1]-1
        if len(A)==2:
            return maxi
        maxitem = max(A[0]-2,A[1]-1)
        for j in range(2,len(A)):
            if A[j] + maxitem > maxi:
                maxi = A[j] + maxitem
            else:
                maxitem = max(maxitem-1,A[j]-1)
        return maxi


s=Solution()
print(s.maxScoreSightseeingPair([4,7,5,8]))