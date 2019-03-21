#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (42.82%)
# Total Accepted:    368.8K
# Total Submissions: 860.2K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
# 
# 
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# But the following [1,2,2,null,3,null,3]  is not:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# Note:
# Bonus points if you could solve it both recursively and iteratively.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


## Recursion
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root,root)
    def isMirror(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return root1.val==root2.val and self.isMirror(root1.left,root2.right) and self.isMirror(root2.left,root1.right)

## First submission: DFS
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left or not root.right:
            if not root.left and not root.right:
                return True
            else: 
                return False
        if root.left.val != root.right.val:
            return False
        stack1 = [root.left]
        stack2 = [root.right]
        def is_same(a,b):
            if not a or not b:
                if not a and not b:
                    return True
                else:
                    return False
            else:
                if a.val == b.val:
                    return True
                else:
                    return False
        while stack1 and stack2:
            cur1 = stack1.pop()
            cur2 = stack2.pop()
            if not is_same(cur1.left,cur2.right) or not is_same(cur1.right,cur2.left):
                return False
            if cur1.left:
                stack1.append(cur1.left)
            if cur1.right:
                stack1.append(cur1.right)
            if cur2.right:
                stack2.append(cur2.right)
            if cur2.left:
                stack2.append(cur2.left)
        return True
            
                
            
            
        

