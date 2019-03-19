#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (47.15%)
# Total Accepted:    241.3K
# Total Submissions: 511K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the postorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [3,2,1]
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return[]
        lst = []
        lst += self.postorderTraversal(root.left)
        lst += self.postorderTraversal(root.right)
        lst.append(root.val)
        return lst

## Iteration
## First do preorderTraversal, but exchange the order of left and right,
## then return the inverse list
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        lst=[]
        while stack:
            cur = stack.pop()
            lst.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return lst[::-1]

## Iteration 2
# mark if the root has been visited or not  
# #https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45725/Simple-Readable-Python-Iterative-Solution    
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [(root,'notvisit')]
        lst=[]
        while stack:
            node, action = stack.pop()
            if action == 'notvisit':
                stack.append((node, 'visited'))
                if node.right:
                    stack.append((node.right, 'notvisit'))
                if node.left:
                    stack.append((node.left, 'notvisit'))
            else:
                # action == 'visited'
                lst.append(node.val)
        return lst