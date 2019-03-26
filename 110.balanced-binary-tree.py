#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (40.46%)
# Total Accepted:    302.1K
# Total Submissions: 745.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as:
# 
# 
# a binary tree in which the depth of the two subtrees of every node never
# differ by more than 1.
# 
# 
# Example 1:
# 
# Given the following tree [3,9,20,null,null,15,7]:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# Return true.
# 
# Example 2:
# 
# Given the following tree [1,2,2,3,3,null,null,4,4]:
# 
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# Return false.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## divide and conquer
## O(NlogN)
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not self.isBalanced(root.left):
            return False
        if not self.isBalanced(root.right):
            return False
        return abs(self.height(root.left)-self.height(root.right))<=1
    def height(self,root):
        if not root:
            return 0
        return max(self.height(root.left),self.height(root.right))+1
        
        
## A better way!
## if we find not balance in the subtree, we can return False
## O(N)
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.flag = True
        self.height(root)
        return self.flag
    
    def height(self,root):
        if not root:
            return 0
        leftheight = self.height(root.left)
        rightheight = self.height(root.right)
        if abs(leftheight-rightheight)>1:
            self.flag = False
        return max(leftheight,rightheight)+1

