#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (34.48%)
# Total Accepted:    130.5K
# Total Submissions: 378.2K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string str, find if str follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
# 
# Example 1:
# 
# 
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# 
# Example 2:
# 
# 
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# 
# Example 3:
# 
# 
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# 
# Example 4:
# 
# 
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# 
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters separated by a single space.
#

# class Solution:
#     def wordPattern(self, pattern: str, str: str) -> bool:
#         list1 = str.split()
#         if len(list1)!=len(pattern):
#             return False
#         else:
#             dict1={}
#             for i in range(len(pattern)):
#                 if not dict1.get(list1[i]):
#                     dict1[list1[i]]=pattern[i]
#                 elif dict1.get(list1[i]) != pattern[i]:
#                     return False
#             if len(set(char for char in pattern)) != len(dict1):
#                 return False
#             return True

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        list1 = str.split()
        if len(list1)!=len(pattern):
            return False
        dict1={}
        pattern_used = []
        for i in range(len(pattern)):
            if list1[i] not in dict1:
                if pattern[i] not in pattern_used:
                    dict1[list1[i]]=pattern[i]
                    pattern_used.append(pattern[i])
                else:
                    return False
            elif dict1.get(list1[i]) != pattern[i]:
                return False
        return True

# s=Solution()
# print(s.wordPattern('abba','dog dog dog dog'))
# print(s.wordPattern('abba',"dog cat cat fish"))
# print(s.wordPattern('abba',"dog cat cat fish"))
