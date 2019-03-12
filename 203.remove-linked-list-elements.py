#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (35.31%)
# Total Accepted:    209K
# Total Submissions: 591.7K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Remove all elements from a linked list of integers that have value val.
# 
# Example:
# 
# 
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## Recursion
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        if head.val == val:
            return self.removeElements(head.next, val)
        else: 
            head.next = self.removeElements(head.next, val)
            return head

## Iteration
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0)
        cur = head
        curnew=dummy
        while cur:
            if cur.val !=val:
                curnew.next = cur
                curnew = curnew.next
            cur=cur.next
        curnew.next = None
        return dummy.next
        
