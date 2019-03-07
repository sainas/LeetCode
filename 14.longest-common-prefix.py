#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (32.95%)
# Total Accepted:    406.1K
# Total Submissions: 1.2M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
#
# Input: ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Note:
#
# All given inputs are in lowercase letters a-z.
#
#


class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if strs == []:
            return ''
        elif len(strs) == 1:
            return strs[0]
        else:
            str1 = strs[0]
            print('str1', str1)
            for i in range(len(str1)):
                print(i)
                for str in strs[1:]:
                    print(str)
                    if len(str) <= i:
                        print(str, 'short')
                        return str1[:i]
                    elif str1[i] != str[i]:
                        print(str, str[i])
                        print('return', str1[:i])
                        return str1[:i]
            print('return', str1)
            return str1


