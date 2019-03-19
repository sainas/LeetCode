#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (45.16%)
# Total Accepted:    213.6K
# Total Submissions: 472.5K
# Testcase Example:  '[1,2,3,null,5]'
#
# Given a binary tree, return all root-to-leaf paths.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# 
# Input:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# Output: ["1->2->5", "1->3"]
# 
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        lst = []
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        if root.left:
            lst += list(map(lambda x:str(root.val)+"->"+x,self.binaryTreePaths(root.left))) 
        if root.right:
            lst += list(map(lambda x:str(root.val)+"->"+x,self.binaryTreePaths(root.right)))
        return lst

## list comprehension: clean code
## https://leetcode.com/problems/binary-tree-paths/discuss/68287/5-lines-recursive-Python/70226
def rootToLeafPaths(self, root):
   if not root: return []
   if not root.left and not root.right: return [str(root.val)]
   return [str(root.val) + '->' + i for i in self.rootToLeafPaths(root.left)] +
             [str(root.val) + '->' + i for i in self.rootToLeafPaths(root.right)]
## list comprehension: very short not so readable
## https://leetcode.com/problems/binary-tree-paths/discuss/68287/5-lines-recursive-Python
def binaryTreePaths(self, root):
    if not root:
        return []
    return [str(root.val) + '->' + path
            for kid in (root.left, root.right) if kid
            for path in self.binaryTreePaths(kid)] or [str(root.val)]
## dfs + stack
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        lst = []
        stack = [(root,str(root.val))]
        while stack:
            cur , path= stack.pop()
            if not cur.left and not cur.right:
                lst.append(path)
            if cur.right: 
                stack.append((cur.right,path + "->" + str(cur.right.val)))
            if cur.left:
                stack.append((cur.left, path + "->" + str(cur.left.val)))
        return lst
## bfs + queue
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        import collections
        if not root:
            return []
        queue = collections.deque([(root,str(root.val))]) 
        lst = []
        while queue:
            cur , path= queue.popleft()
            if not cur.left and not cur.right:
                lst.append(path)
            if cur.left:
                queue.append((cur.left, path + "->" + str(cur.left.val)))
            if cur.right: 
                queue.append((cur.right,path + "->" + str(cur.right.val)))        
        return lst
               