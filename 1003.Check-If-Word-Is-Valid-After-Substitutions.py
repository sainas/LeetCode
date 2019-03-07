class Solution:
    def isValid(self, S: str) -> bool:
        if len(S)%3!=0 or S[0]!='a'or S[-1]!='c':
            return False
        p1=0
        l1=[]
        while(p1<len(S)):
            if S[p1]=='c' and l1[-1]=='ab':
                l1.pop()
                p1 +=1
            elif S[p1:p1+2]=='bc' and l1[-1]=='a':
                l1.pop()
                p1+=2
            elif S[p1:p1+2]=='ba' and l1[-1]=='a':
                p1+=1
                l1[-1]='ab'
            elif S[p1:p1+3]=='abc':
                p1+=3
            elif S[p1:p1+3]=='aba':
                p1+=2
                l1.append('ab')
            elif S[p1:p1+2]=='aa':
                p1+=1
                l1.append('a')
            else:
                return False
        return l1==[]    

# S=Solution()
# ST="aabcbc"
# ST2="ababcabcc"
# ST3="abaabcbcc"
# ST4="aabcbabcc"
# print(S.isValid(ST))
# print(S.isValid(ST2))
# print(S.isValid(ST3))
# print(S.isValid(ST4))