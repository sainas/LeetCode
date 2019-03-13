#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (30.66%)
# Total Accepted:    784.8K
# Total Submissions: 2.6M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## My iteration
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        flag = 0
        while l1 or l2:
            if l1 and l2:
                cur.next = l1
                cur = cur.next
                cur.val +=l2.val
                l1, l2 = l1.next, l2.next
            else: 
                cur.next = l1 if l1 else l2
                cur = cur.next
                l1 = l1.next if l1 else l1
                l2 = l2.next if l2 else l2
            if flag:
                cur.val += 1
            flag = cur.val//10
            cur.val = cur.val%10
        if flag:
            cur.next = ListNode(1)
        return dummy.next
## clean iteration: new ListNode everytime 
class Solution:
# @return a ListNode
def addTwoNumbers(self, l1, l2):
    carry = 0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1+v2+carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next
## Clean Iteration: add a parameter in the function
class Solution(object):
    def addTwoNumbers(self, l1, l2, carry=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None if not carry else ListNode(1)
        l1 = l1 or ListNode(0)
        l2 = l2 or ListNode(0)
        value = l1.val + l2.val + carry
        carry = 1 if value > 9 else 0
        node = ListNode(value % 10)
        node.next = self.addTwoNumbers(l1.next, l2.next, carry=carry)
        return node
## Recursion
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        l1.val += l2.val
        l1.next = self.addTwoNumbers(l1.next,l2.next)
        if l1.val >=10:
            l1.next = self.addTwoNumbers(l1.next,ListNode(1))
            l1.val = l1.val%10
        return l1    
