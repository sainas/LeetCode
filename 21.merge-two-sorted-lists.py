#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (46.00%)
# Total Accepted:    520.8K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## Pointer
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        else:
            
            dummy = ListNode(0)
            cur = dummy
            while (l1!=None or l2!=None):
                if not l1:
                    cur.next = l2
                    l2 = l2.next
                elif not l2:
                    cur.next = l1
                    l1 = l1.next
                elif l1.val>l2.val:
                    cur.next = l2
                    l2 = l2.next
                else:
                    cur.next = l1
                    l1 = l1.next
                cur=cur.next      
            return dummy.next

## Recursion
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        else:
            if l1.val>l2.val:
                cur = l2
                cur.next = self.mergeTwoLists(l1,l2.next)
                return cur
            else:
                cur = l1
                cur.next = self.mergeTwoLists(l1.next,l2)
                return cur
        
## 网上找的，更简洁一些，把判断None的条件放在最后
class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        ret_head = ListNode(0)
        
        trav_head = ret_head
        
        #while both list still have nodes
        while l1 and l2:
            #the node with smaller value will be put in the return list first, 
            if l1.val <= l2.val:
                trav_head.next = l1
                l1 = l1.next
            else:
                trav_head.next = l2
                l2 = l2.next
            #remember to precess the new list as well !!!!!
            trav_head = trav_head.next
        #now one of the lists is empty, we just need to append the list is not empty into the return list
        
        if l1:
            trav_head.next = l1
        else:
            trav_head.next = l2
        
        return ret_head.next
        
        
# ## Test
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




# s=Solution()
# input =stringToIntegerList([1,2,3,4])
# head = stringToListNode(input)
# output = s.mergeTwoLists(head,head)
# print(listNodeToString(output))



