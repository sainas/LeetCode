#
# @lc app=leetcode id=1007 lang=python3
#
# [1007] Minimum Domino Rotations For Equal Row
#
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/description/
#
# algorithms
# Medium (48.58%)
# Total Accepted:    4.5K
# Total Submissions: 9.5K
# Testcase Example:  '[2,1,2,4,2,2]\n[5,2,6,2,3,2]'
#
# In a row of dominoes, A[i] and B[i] represent the top and bottom halves of
# the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on
# each half of the tile.)
# 
# We may rotate the i-th domino, so that A[i] and B[i] swap values.
# 
# Return the minimum number of rotations so that all the values in A are the
# same, or all the values in B are the same.
# 
# If it cannot be done, return -1.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
# Output: 2
# Explanation: 
# The first figure represents the dominoes as given by A and B: before we do
# any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the
# top row equal to 2, as indicated by the second figure.
# 
# 
# Example 2:
# 
# 
# Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
# Output: -1
# Explanation: 
# In this case, it is not possible to rotate the dominoes to make one row of
# values equal.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A[i], B[i] <= 6
# 2 <= A.length == B.length <= 20000
# 
# 
#

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
