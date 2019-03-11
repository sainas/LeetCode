#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (34.86%)
# Total Accepted:    129.4K
# Total Submissions: 371.1K
# Testcase Example:  '3'
#
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1 ... n.
# 
# Example:
# 
# 
# Input: 3
# Output:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## Dynamic Programming
## 我写的超慢版本
class Solution:
    cache={}
    def generateTrees(self, n: int) :
        from copy import deepcopy
        if n ==1:
            return [TreeNode(1)]
        if n ==0:
            return []
        dp=[[]]*(n+1)
        dp[0]= [None]
        dp[1]=[TreeNode(1)]
        dp2=[[]]*(n+1)
        dp2[0]= [None]
        dp2[1]= [1]
        
        for i in range(2,n+1):
            for j in range(i):
                for k1 in dp[j]:
                    for k2 in dp[i-j-1]:
                        Tree = TreeNode(j+1)
                        Tree.left = k1
                        if not k2:
                            Tree.right = k2
                        else:
                            copytree = deepcopy(k2)
                            self.generatenewtree(copytree,j+1)
                            Tree.right = copytree
                        dp[i]=dp[i]+[Tree]
                        dp2[i]=dp2[i]+[j+1]
        return dp[n]

    def generatenewtree(self,tree,n):
        if tree:
            tree.val +=n
            self.generatenewtree(tree.left,n)
            self.generatenewtree(tree.right,n)
        

# s=Solution()
# print(s.generateTrees(3).val)
        

