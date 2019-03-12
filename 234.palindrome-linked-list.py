#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (35.38%)
# Total Accepted:    235K
# Total Submissions: 664.2K
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Example 1:
# 
# 
# Input: 1->2
# Output: false
# 
# Example 2:
# 
# 
# Input: 1->2->2->1
# Output: true
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## 复杂度比较高的解法
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return lst==lst[::-1]
        
## space O(1)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slowp1=head
        slowp2=head.next
        slowp3=head.next.next
        fast=head.next
        head.next = None
        if not slowp3:
            return slowp1.val==slowp2.val
        while fast and fast.next:
            fast = fast.next.next
            slowp2.next = slowp1
            slowp1 = slowp2
            slowp2 = slowp3
            slowp3 = slowp3.next
        if not fast: 
            slowp1 = slowp1.next
        while slowp1:
            if slowp1.val!=slowp2.val:
                return False
            slowp1 = slowp1.next
            slowp2 = slowp2.next
        return True  


## space O(1): 更简洁
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        p1=None
        p2=head
        p3=head.next
        fast=head
        while fast and fast.next:
            fast = fast.next.next
            p2.next = p1
            p1,p2,p3 = p2,p3,p3.next
        if fast: # odd
            p2 = p2.next
        while p1:
            if p1.val!=p2.val:
                return False
            p1, p2 = p1.next, p2.next
        return True

