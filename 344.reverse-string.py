#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#
# https://leetcode.com/problems/reverse-string/description/
#
# algorithms
# Easy (62.72%)
# Total Accepted:    379.3K
# Total Submissions: 604.2K
# Testcase Example:  '["h","e","l","l","o"]'
#
# Write a function that reverses a string. The input string is given as an
# array of characters char[].
# 
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
# 
# You may assume all the characters consist of printable ascii characters.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# 
# 
# 
# Example 2:
# 
# 
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
# 
# 
# 
# 
#

# Recursion 
# class Solution:
#     def reverseString(self, s) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         self.helper(0, len(s)-1,s)

#     def helper(self, start, end, s):
#         if start<end:
#             s[start], s[end] = s[end], s[start]
#             self.helper(start+1, end-1, s)   

# class Solution:
#     def reverseString(self, s) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         s[::1]= s[::-1]

class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        

