#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (50.35%)
# Total Accepted:    309.8K
# Total Submissions: 614.8K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the preorder traversal of its nodes' values.
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
# Output: [1,2,3]
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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        lst = [root.val]
        lst += self.preorderTraversal(root.left)
        lst += self.preorderTraversal(root.right)                     
        return lst        

## Iteration
## First append itself then go left if None go right if both none stack pop
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        lst = []
        stack = []
        cur = root
        while stack or cur :
            if not cur:
                cur = stack.pop()
                cur = cur.right
            else:
                lst.append(cur.val)
                if cur.left:
                    stack.append(cur)
                    cur = cur.left
                else:
                    cur = cur.right   
        return lst

## Iteration
## Cleaner: every loop if left go left, else pop and go right nond, then loop
def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        lst = []
        stack = []
        cur = root
        while stack or cur :
            while cur:
                lst.append(cur.val)
                stack.append(cur)
                cur = cur.left
            if stack:
                cur = stack.pop()
                cur = cur.right
        return lst
                
##Iteration
##Much more clean
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        lst=[]
        while stack:
            cur = stack.pop()
            lst.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return lst
        