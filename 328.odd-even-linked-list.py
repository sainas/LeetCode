#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#
# https://leetcode.com/problems/odd-even-linked-list/description/
#
# algorithms
# Medium (48.21%)
# Total Accepted:    135.3K
# Total Submissions: 280.5K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given a singly linked list, group all odd nodes together followed by the even
# nodes. Please note here we are talking about the node number and not the
# value in the nodes.
# 
# You should try to do it in place. The program should run in O(1) space
# complexity and O(nodes) time complexity.
# 
# Example 1:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
# 
# 
# Example 2:
# 
# 
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL
# 
# 
# Note:
# 
# 
# The relative order inside both the even and odd groups should remain as it
# was in the input.
# The first node is considered odd, the second node even and so on ...
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        po = head
        pe = head.next
        cur = head.next
        pehead = head.next
        while 1:
            cur = cur.next
            if not cur: break
            po.next = cur
            po = po.next
            cur = cur.next
            if not cur: break
            pe.next = cur
            pe = pe.next
        po.next = pehead
        pe.next = None
        return head

##稍微简洁了一点
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        po = head
        pe = head.next
        pehead = head.next
        while pe.next:
            po.next = pe.next
            po = po.next
            pe.next = po.next
            pe = pe.next
            if not pe:break
        po.next = pehead
        return head
