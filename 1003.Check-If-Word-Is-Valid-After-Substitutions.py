#
# @lc app=leetcode id=1003 lang=python3
#
# [1003] Check If Word Is Valid After Substitutions
#
# https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/description/
#
# algorithms
# Medium (52.24%)
# Total Accepted:    6K
# Total Submissions: 11.4K
# Testcase Example:  '"aabcbc"'
#
# We are given that the string "abc" is valid.
# 
# From any valid string V, we may split V into two pieces X and Y such that X +
# Y (X concatenated with Y) is equal to V.  (X or Y may be empty.)  Then, X +
# "abc" + Y is also valid.
# 
# If for example S = "abc", then examples of valid strings are: "abc",
# "aabcbc", "abcabc", "abcabcababcc".  Examples of invalid strings are:
# "abccba", "ab", "cababc", "bac".
# 
# Return true if and only if the given string S is valid.
# 
# 
# 
# Example 1:
# 
# 
# Input: "aabcbc"
# Output: true
# Explanation: 
# We start with the valid string "abc".
# Then we can insert another "abc" between "a" and "bc", resulting in "a" +
# "abc" + "bc" which is "aabcbc".
# 
# 
# 
# Example 2:
# 
# 
# Input: "abcabcababcc"
# Output: true
# Explanation: 
# "abcabcabc" is valid after consecutive insertings of "abc".
# Then we can insert "abc" before the last letter, resulting in "abcabcab" +
# "abc" + "c" which is "abcabcababcc".
# 
# 
# 
# Example 3:
# 
# 
# Input: "abccba"
# Output: false
# 
# 
# 
# Example 4:
# 
# 
# Input: "cababc"
# Output: false
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= S.length <= 20000
# S[i] is 'a', 'b', or 'c'
# 
# 
# 
# 
# 
# 
# 
# 
# 
#

class Solution:
    def isValid(self, S: str) -> bool:
        if len(S)%3!=0 or S[0]!='a'or S[-1]!='c':
            return False
        p1=0
        l1=[]
        while(p1<len(S)):
            if S[p1]=='c' and l1[-1]=='ab':
                l1.pop()
                p1 +=1
            elif S[p1:p1+2]=='bc' and l1[-1]=='a':
                l1.pop()
                p1+=2
            elif S[p1:p1+2]=='ba' and l1[-1]=='a':
                p1+=1
                l1[-1]='ab'
            elif S[p1:p1+3]=='abc':
                p1+=3
            elif S[p1:p1+3]=='aba':
                p1+=2
                l1.append('ab')
            elif S[p1:p1+2]=='aa':
                p1+=1
                l1.append('a')
            else:
                return False
        return l1==[]    

# S=Solution()
# ST="aabcbc"
# ST2="ababcabcc"
# ST3="abaabcbcc"
# ST4="aabcbabcc"
# print(S.isValid(ST))
# print(S.isValid(ST2))
# print(S.isValid(ST3))
# print(S.isValid(ST4))


