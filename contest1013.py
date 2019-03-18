
##1013. Pairs of Songs With Total Durations Divisible by 60

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dct = {}
        for i in range(len(time)):
            rest = time[i]%60
            dct[rest] = dct.get(rest,0)+1
        flag = 0
        for i in range(1,30):
            flag += dct.get(i,0)*dct.get(60-i,0)
        if dct.get(30,0)>1:
            flag += dct.get(30,0)*(dct.get(30,0)-1)//2
        if dct.get(0,0)>1:
            flag += dct.get(0,0)*(dct.get(0,0)-1)//2
        return flag
