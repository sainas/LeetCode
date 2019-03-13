#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (26.55%)
# Total Accepted:    179.7K
# Total Submissions: 676K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, rotate the list to the right by k places, where k is
# non-negative.
# 
# Example 1:
# 
# 
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# 
# 
# Example 2:
# 
# 
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

### 可能是对的的答案但是超过time limit 了，考虑两个edge case：
### [1] 0    
### [1,2,3] 20000000
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not k:
            return head
        fast = head
        while fast:
            fast = fast.next
            k-=1
            if not k:
                if not fast:
                    return head
                else:
                    break
            if not fast:
                fast = head
        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next
        fast.next = head
        newhead = slow.next
        slow.next = None
        return newhead

## Solution
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        if not k:
            return head
        cur = head
        lenth = 1
        while cur.next:
            cur = cur.next
            lenth += 1
        steps = k%lenth
        if not steps:
            return head
        else:
            cur.next = head
            for _ in range(lenth-steps-1):
                head=head.next
            newhead = head.next
            head.next = None
            return newhead
           

