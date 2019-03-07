#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (30.11%)
# Total Accepted:    320.5K
# Total Submissions: 1.1M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
# 
# Example 1:
# 
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "race a car"
# Output: false
# 
# 
#

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         i = 0
#         j = len(s)-1
#         while(i < j):
#             while(i<j and not s[i].isalnum()):
#                 i += 1
#             while(i<j and not s[j].isalnum()):
#                 j -= 1
#             if s[i].lower()!=s[j].lower():
#                 return False
#             i += 1
#             j -= 1
#         return True

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s ="".join(char for char in s if char.isalnum())
#         return s.lower()==s[::-1].lower()
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[\W+]', '', s)
        return s.lower()==s[::-1].lower()

# s=Solution()
# print(s.isPalindrome('A man, a plan, a canal: Panama'))
# print(s.isPalindrome('""""'))
# print(s.isPalindrome('"a."'))
# print(s.isPalindrome('"a a"'))
# print(s.isPalindrome("a a"))
# print(s.isPalindrome(" @#%a&*(aab"))
# print(s.isPalindrome(""))
# print(s.isPalindrome('"0P"'))

