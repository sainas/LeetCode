# class Solution:
#     def minDominoRotations(self, A,B) -> int:
#         def swaptimes(A,B,target):
#             swapatob = 0
#             swapbtoa = 0 
#             for i in range(len(A)):
#                 if not target in (A[i],B[i]) :
#                     return -1
#                 swapbtoa += (A[i]!=target and B[i] == target)
#                 swapatob += (B[i]!=target and A[i] == target)
#             return min(swapatob,swapbtoa)
#         swap1 = swaptimes(A,B,A[0])
#         swap2 = swaptimes(A,B,B[0])
#         if min(swap1,swap2) == -1:
#             return max(swap1,swap2)
#         else:
#             return min(swap1,swap2)


## 网上的方法
# class Solution:
#     def minDominoRotations(self, A, B):
#         for x in range(1, 7):
#             if all(x == a or x == b for a, b in zip(A, B)):
#                 return min(len(A) - A.count(x), len(B) - B.count(x))
#         return -1

class Solution:
    def minDominoRotations(self, A, B):
        from functools import reduce
        # s = reduce(set.__and__, [set(d) for d in zip(A, B)])
        s = reduce(lambda x, y:x and y, [set(d) for d in zip(A, B)])
        if not s: return -1
        x = s.pop()
        return min(len(A) - A.count(x), len(B) - B.count(x))

## test
s= Solution()
print(s.minDominoRotations([1,2,1,2,1],[2,1,2,1,2]))
