#
# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#
# https://leetcode.com/problems/k-th-symbol-in-grammar/description/
#
# algorithms
# Medium (37.73%)
# Total Accepted:    10.8K
# Total Submissions: 28.7K
# Testcase Example:  '1\n1'
#
# On the first row, we write a 0. Now in every subsequent row, we look at the
# previous row and replace each occurrence of 0 with 01, and each occurrence of
# 1 with 10.
# 
# Given row N and index K, return the K-th indexed symbol in row N. (The values
# of K are 1-indexed.) (1 indexed).
# 
# 
# Examples:
# Input: N = 1, K = 1
# Output: 0
# 
# Input: N = 2, K = 1
# Output: 0
# 
# Input: N = 2, K = 2
# Output: 1
# 
# Input: N = 4, K = 5
# Output: 1
# 
# Explanation:
# row 1: 0
# row 2: 01
# row 3: 0110
# row 4: 01101001
# 
# 
# Note:
# 
# 
# N will be an integer in the range [1, 30].
# K will be an integer in the range [1, 2^(N-1)].
# 
# 
#
# class Solution:
#     def kthGrammar(self, N: int, K: int) -> int:
#         list = [[0,1],[1,0]]
#         from functools import reduce
#         return reduce(lambda x, y: list[int(x)][int(y)],bin(K-1)[2:].zfill(N),0)

## 网上比较好的答案
# class Solution(object):
#     def kthGrammar(self, N, K):
#         return bin(K-1).count('1')%2

## Recursion
class Solution(object):
    def kthGrammar(self, N, K):
        if N == 0: return 0
        return K&1 if self.kthGrammar(N-1, (K+1)>>1) else int(not K&1)
## K&1 == 1 表示是奇数，parent是0时奇数为0, 不一样，所以parent为1时可以K&1

## WRONG ANSWER!!! Time limit exceeded
# class Solution:
#     def kthGrammar(self, N: int, K: int) -> int:
#         row = '0'
#         if N>1:
#             for _ in range(N-1):
#                 newrow = ""
#                 for i in row:
#                     if i == "0":
#                         newrow += '01'
#                     else:
#                         newrow += '10'
#                 row = newrow
#         return int(row[K-1])

       
s = Solution()
# print(s.kthGrammar(1,1))
assert s.kthGrammar(1,1)==0
assert s.kthGrammar(2,1)==0
assert s.kthGrammar(2,2)==1
assert s.kthGrammar(4,5)==1


