#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (47.26%)
# Total Accepted:    345.4K
# Total Submissions: 729.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## First version:
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        lst = [[root.val]]
        parentlevel = [root]
        childlevel=[]
        while parentlevel:
            for node in parentlevel:
                if node.left:
                    childlevel.append(node.left)
                if node.right:
                    childlevel.append(node.right)
            if childlevel:
                lst.append(list(x.val for x in childlevel))
                parentlevel = childlevel
                childlevel = []
            else: break
        return lst
        
        
        

