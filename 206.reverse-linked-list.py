#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (52.52%)
# Total Accepted:    523.7K
# Total Submissions: 989.5K
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# 
# 
# Follow up:
# 
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
# 
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

## recursion
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         rev = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return rev


## iteration     
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur1 = head
        cur2 = cur1.next
        cur1.next = None
        while cur2.next!=None:
            cur3 = cur2.next
            cur2.next = cur1
            cur1 = cur2
            cur2 = cur3
        cur2.next=cur1
        return cur2

## Test


def stringToIntegerList(input):
    return input

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"





input =stringToIntegerList([1,2,3,4])
head = stringToListNode(input)
s=Solution()
output = s.reverseList(head)
print(listNodeToString(output))


 

