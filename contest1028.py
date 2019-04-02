class Solution:
    def baseNeg2(self, N: int) -> str:
        if not N:
            return "0"
        lst=[]
        while N:
            N,rem=divmod(N,-2)
            if rem<0:
                rem=1
                N+=1
            lst.append(str(rem))
        return "".join(lst)[::-1]