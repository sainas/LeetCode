#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (41.88%)
# Total Accepted:    187K
# Total Submissions: 443.4K
# Testcase Example:  '3'
#
# Given a non-negative index k where k ≤ 33, return the k^th index row of the
# Pascal's triangle.
# 
# Note that the row index starts from 0.
# 
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
# 
# Example:
# 
# 
# Input: 3
# Output: [1,3,3,1]
# 
# 
# Follow up:
# 
# Could you optimize your algorithm to use only O(k) extra space?
# 

##Recursion
# class Solution:
#     def getRow(self, rowIndex: int):
#         if rowIndex ==0:
#             return [1]
#         pre_row=self.getRow(rowIndex-1)
#         return list(map(lambda x,y:x+y, [0]+pre_row, pre_row+[0]))    


class Solution:
    def getRow(self, rowIndex: int):
        row = [1]
        for _ in range(rowIndex):
            row = list(map(lambda x,y:x+y, [0]+row, row+[0]))    
        return row
# s=Solution()
# print(s.getRow(3))