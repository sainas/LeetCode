#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (33.24%)
# Total Accepted:    356.4K
# Total Submissions: 1.1M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
# 
# Example:
# 
# 
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


## Time limit exceed 
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         lst = list(filter(None,lists)) 
#         if not lst:
#             return None
#         lists = lst
#         dummyhead = ListNode(0)
#         cur = dummyhead
#         while lists:
#             valuelst = [node.val for node in lists]
#             for index,value in enumerate(valuelst):
#                 if value == min(valuelst):
#                     cur.next = lists[index]
#                     cur = cur.next
#                     lists[index]=lists[index].next
#                     if not lists[index]:
#                         lists.pop(index)
#                     break
#         return dummyhead.next
            
## Very long time: recursion
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists)==1:
            return lists[0]
        lst1 = lists[0]
        lst2 = self.mergeKLists(lists[1:])
        dummyhead = ListNode(0)
        cur = dummyhead
        while lst1 and lst2:
            if lst1.val < lst2.val:
                cur.next = lst1
                lst1=lst1.next
            else:
                cur.next = lst2
                lst2=lst2.next
            cur=cur.next  
        if not lst1 or not lst2:
            cur.next = lst1 if lst1 else lst2
        return dummyhead.next

## Iteration: very slow
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import functools
        if not lists:
            return None
        if len(lists)==1:
            return lists[0]
        head = functools.reduce(self.merge2,lists)
        return head
    def merge2(self,lst1,lst2):
        dummyhead = ListNode(0)
        cur = dummyhead
        while lst1 and lst2:
            if lst1.val < lst2.val:
                cur.next = lst1
                lst1=lst1.next
            else:
                cur.next = lst2
                lst2=lst2.next
            cur=cur.next  
        if not lst1 or not lst2:
            cur.next = lst1 if lst1 else lst2
        return dummyhead.next

## Sort numbers            
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists)==1:
            return lists[0]
        value=[]
        for node in lists:
            while node:
                value.append(node.val)
                node = node.next
        dummyhead = ListNode(0)
        cur = dummyhead
        for val in sorted(value):
            cur.next = ListNode(val)
            cur = cur.next
        return dummyhead.next
            
## PriorityQueue
# O(Nlogk) 
# TypeError '<' not supported between instances of 'ListNode' and 'ListNode':
# This error occurs because ListNode definition does not include __lt__ method. 
# To avoid this error, we can use a wrapper class with __lt__ method for ListNode.
# https://leetcode.com/problems/merge-k-sorted-lists/solution/
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        class Wrapper():
            def __init__(self, node):
                self.node = node
            def __lt__(self,other):
                return self.node.val < other.node.val
        from queue import PriorityQueue
        dummy = ListNode(0)
        cur = dummy
        pq = PriorityQueue()
        for node in lists:
            if node:
                pq.put(Wrapper(node))
        while not pq.empty():
            node = pq.get().node
            cur.next = node
            cur = cur.next
            node = node.next
            if node:
                pq.put(Wrapper(node))
        return dummy.next
## Divide and conquer
#  O(Nlogk)                                         
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists)==1:
            return lists[0]
        for i in range(len(lists)//2):
            lists[2*i]=self.merge2(lists[2*i],lists[2*i+1])
        lists = lists[::2]  
        return self.mergeKLists(lists)
            
    def merge2(self,lst1,lst2):
        dummyhead = ListNode(0)
        cur = dummyhead
        while lst1 and lst2:
            if lst1.val < lst2.val:
                cur.next = lst1
                lst1=lst1.next
            else:
                cur.next = lst2
                lst2=lst2.next
            cur=cur.next  
        if not lst1 or not lst2:
            cur.next = lst1 if lst1 else lst2
        return dummyhead.next

## Heap
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        from heapq import heappush, heappop
        heap = []
        for node in lists:
            while node:
                heappush(heap,node.val)
                node = node.next
        dummy = ListNode(0)
        cur = dummy
        while heap:
            cur.next = ListNode(heappop(heap))
            cur = cur.next
        return dummy.next            
            
            
            
              