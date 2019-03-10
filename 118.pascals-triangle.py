#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (44.38%)
# Total Accepted:    230.8K
# Total Submissions: 516.5K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 5
# Output:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
# 
#
class Solution:
    def generate(self, numRows: int):
        if numRows ==0:
            return []
        if numRows ==1:
            return [[1]]
        pre_tri = self.generate(numRows-1)
        last_row = list(map(lambda x,y:x+y, [0] + pre_tri[-1] , pre_tri[-1]+[0]))
        return pre_tri + [last_row]


