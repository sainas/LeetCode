class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        lst = [A[0]]
        for i in range(1,len(A)):
          lst.append(lst[i-1]+A[i])
        if lst[-1] % 3 ==0:
            for i in range(len(lst)):
                if lst[i]==lst[-1]/3:
                    for j in range(i,len(lst)):
                        if lst[j] == 2*lst[-1]/3:
                            return True
        return False