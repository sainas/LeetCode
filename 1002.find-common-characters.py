#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#
# https://leetcode.com/problems/find-common-characters/description/
#
# algorithms
# Easy (68.46%)
# Total Accepted:    9.8K
# Total Submissions: 14.3K
# Testcase Example:  '["bella","label","roller"]'
#
# Given an array A of strings made only from lowercase letters, return a list
# of all characters that show up in all strings within the list (including
# duplicates).  For example, if a character occurs 3 times in all strings but
# not 4 times, you need to include that character three times in the final
# answer.
# 
# You may return the answer in any order.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["bella","label","roller"]
# Output: ["e","l","l"]
# 
# 
# 
# Example 2:
# 
# 
# Input: ["cool","lock","cook"]
# Output: ["c","o"]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] is a lowercase letter
# 
# 
# 
#
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if len(A) == 1:
            return [letter for letter in A[0]]
        dict1={}
        for letter in A[0]:
            dict1[letter]=dict1.get(letter,0)+1
        dict2 = dict1.copy()
        for str1 in A[1:]:
            for letter in str1:
                dict2[letter]=dict2.get(letter,-105)-1
            for k in [*dict2]:
                if dict2[k]==dict1.get(k,'None'):
                    dict1.pop(k, None)
                elif dict2[k]>0:
                    dict1[k]=dict1[k]-dict2[k]
            dict2=dict1.copy()
        result=[]
        for k in [*dict1]:
            for i in range(dict1[k]):
                result.append(k)
        return result
