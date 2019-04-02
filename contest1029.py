class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        lst=[]
        ans=0
        for i in A:
            ans=(ans<<1)+i
            lst.append(ans % 5 ==0)
        return lst