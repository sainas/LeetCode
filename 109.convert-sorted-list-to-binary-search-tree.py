#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (39.75%)
# Total Accepted:    167.8K
# Total Submissions: 420.2K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# Example:
# 
# 
# Given the sorted linked list: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


## Recursion: Space Complexity is kinda big, should use index instead of slicing
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        lst=self.linkedlist2list(head)
        return self.lst2BST(lst)
    def lst2BST(self,lst):    
        if not lst:
            return None
        if len(lst)==1:
            return TreeNode(lst[0])
        rootindex = len(lst)//2
        root = TreeNode(lst[rootindex])
        root.left = self.lst2BST(lst[:rootindex])
        root.right = self.lst2BST(lst[rootindex+1:])
        return root
    
    def linkedlist2list(self,head):
        lst=[]
        while head:
            lst.append(head.val)
            head = head.next
        return lst
        

## Recursion:
# Using index but no difference in speed and space
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        self.lst=self.linkedlist2list(head)
        return self.lst2BST(0,len(self.lst)-1)
    
    def lst2BST(self,start,end):    
        if start > end:
            return None
        if start == end:
            return TreeNode(self.lst[start])
        rootindex = (start+end)//2
        root = TreeNode(self.lst[rootindex])
        root.left = self.lst2BST(start,rootindex-1)
        root.right = self.lst2BST(rootindex+1,end)
        return root
    
    def linkedlist2list(self,head):
        lst=[]
        while head:
            lst.append(head.val)
            head = head.next
        return lst
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## Inorder simulator:
## https://leetcode.com/articles/convert-sorted-list-to-binary-search-tree/
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        self.head = head
        return self.convert(1,self.sizelist())
    def convert(self, start, end):
        if start>end: return None
        mid = (start+end)//2
        left = self.convert(start,mid-1)
        root = TreeNode(self.head.val)
        root.left = left
        self.head=self.head.next
        root.right = self.convert(mid+1,end)
        return root
        
    def sizelist(self):
        temp =  self.head
        size = 0
        while temp:
            temp = temp.next
            size +=1
        return size
    