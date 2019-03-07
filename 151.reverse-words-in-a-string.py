#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#
# https://leetcode.com/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (15.83%)
# Total Accepted:    257.1K
# Total Submissions: 1.6M
# Testcase Example:  '"the sky is blue"'
#
# Given an input string, reverse the string word by word.
# 
# 
# 
# Example 1:
# 
# 
# Input: "the sky is blue"
# Output: "blue is sky the"
# 
# 
# Example 2:
# 
# 
# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing
# spaces.
# 
# 
# Example 3:
# 
# 
# Input: "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single
# space in the reversed string.
# 
# 
# 
# 
# Note:
# 
# 
# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces. However, your reversed
# string should not contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single space in the
# reversed string.
# 
# 
# 
# 
# Follow up:
# 
# For C programmers, try to solve it in-place in O(1) extra space.
#

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         list1=s.split()
#         revstr = " ".join(list1[::-1])
#         return revstr  

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return " ".join(list(filter(lambda x: x!='',s.split(" ")))[::-1])

class Solution(object):
    def reverseWords(self, s)  -> str:
        list1 = s.split(" ")
        return " ".join(word for word in list1[::-1] if word)

# s=Solution()
# print(s.reverseWords('the sky is blue'))  
# print(s.reverseWords("  hello world!  ")) 
# print(s.reverseWords("a good   example"))
