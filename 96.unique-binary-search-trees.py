#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (45.20%)
# Total Accepted:    186.7K
# Total Submissions: 412.9K
# Testcase Example:  '3'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1 ... n?
# 
# Example:
# 
# 
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# # 
# # Recursion with memorization
# ## 不用cache就会超时！
# ## cache错误地放在函数里面的话，也超时！！
# ## cache一定要放在函数外面
# class Solution:
#     cache = {0:1,1:1}
#     def numTrees(self, n: int) -> int:
#         if n in self.cache:
#             return self.cache[n]
#         else:
#             self.cache[n]=0
#             for i in range(n):
#                 self.cache[n] += self.numTrees(i)*self.numTrees(n-1-i)
#             return self.cache[n]

# Dynamic Programming
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(i):
                dp[i]+=dp[j]*dp[i-j-1]
        return dp[n]
       

# s=Solution()
# print(s.numTrees(19))       

