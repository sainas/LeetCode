#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (59.31%)
# Total Accepted:    461.3K
# Total Submissions: 777.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its depth = 3.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## My code
# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         elif not root.left and not root.right:
#             return 1
#         else:
#             return 1+max(self.maxDepth(root.left) , self.maxDepth(root.right))

## From internet
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 1+max(self.maxDepth(root.left) , self.maxDepth(root.right)) if root else 0
 
## Iteration
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        import collections
        if not root:
            return 0
        queue = collections.deque([(root,1)])
        while queue:
            cur, depth = queue.popleft()
            if cur.left:
                queue.append((cur.left,depth+1))
            if cur.right:
                queue.append((cur.right,depth+1))
            
        return depth
        

