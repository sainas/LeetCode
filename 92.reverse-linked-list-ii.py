#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (34.18%)
# Total Accepted:    183.7K
# Total Submissions: 535.4K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
# 
# Note: 1 ≤ m ≤ n ≤ length of list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## First Submission
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        dummyhead = ListNode(0)
        dummyhead.next  = head
        p1 = dummyhead
        for _ in range(m-1):
            p1  = p1.next
        p2 = p1.next
        p3 = p2.next
        for _ in range(n-m):
            p2,p2.next,p3 = p3,p2,p3.next
        p1.next.next = p3
        p1.next = p2
        return dummyhead.next
           
## Iteration
#https://leetcode.com/problems/reverse-linked-list-ii/discuss/30709/Talk-is-cheap-show-me-the-code-(and-DRAWING)
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        dummyhead = ListNode(0)
        dummyhead.next  = head
        p1 = dummyhead
        for _ in range(m-1):
            p1  = p1.next
        p2 = p1.next
        for _ in range(n-m):
            p1.next, p2.next.next,p2.next=p2.next,p1.next,p2.next.next
        return dummyhead.next

## A bad recursion: This is not O(N)!!!
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m >= n:
            return head
        p1 = head
        p2 = head
        for _ in range(m-1):
            p1  = p1.next
        for _ in range(n-1):
            p2  = p2.next
        p1.val, p2.val = p2.val, p1.val
        
        return self.reverseBetween(head,m+1,n-1)

## Recursion O(n), not very intuitive
# https://leetcode.com/articles/reverse-linked-list-ii/                
