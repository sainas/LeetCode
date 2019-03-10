#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (43.00%)
# Total Accepted:    284.2K
# Total Submissions: 656.8K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
# 
# Example:
# 
# 
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## Recursion 

# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         p1 = head
#         p2 = head.next
#         p3 = head.next.next
#         head = p2
#         head.next = p1
#         head.next.next = self.swapPairs(p3)
#         return head

# class Solution:
#     def swapPairs(self, head):
#         if not head or not head.next:
#             return head
#         cur = head
#         head = cur.next
#         cur.next = self.swapPairs(head.next)
#         head.next = cur
#         return head
    
## Loop
class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        newhead = head.next
        cur = head
        while (not cur or not cur.next):
            p1 = cur
            p2 = cur.next.next
            cur = cur.next
            cur.next = p1
            cur.next.next = p2
            cur = cur.next.next
        return newhead

## Test
# def stringToIntegerList(input):
#     return input

# def stringToListNode(input):
#     # Generate list from the input
#     numbers = stringToIntegerList(input)

#     # Now convert that list into linked list
#     dummyRoot = ListNode(0)
#     ptr = dummyRoot
#     for number in numbers:
#         ptr.next = ListNode(number)
#         ptr = ptr.next

#     ptr = dummyRoot.next
#     return ptr

# def listNodeToString(node):
#     if not node:
#         return "[]"
#     result = ""
#     while node:
#         result += str(node.val) + ", "
#         node = node.next
#     return "[" + result[:-2] + "]"

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



# input =stringToIntegerList([1,2,3,4])
# head = stringToListNode(input)
# output = swapPairs(head)
# print(listNodeToString(output))


