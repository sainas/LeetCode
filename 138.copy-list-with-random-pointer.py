#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (25.86%)
# Total Accepted:    226.3K
# Total Submissions: 873.7K
# Testcase Example:  '{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}'
#
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
# 
# Return a deep copy of the list.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input:
# 
# {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
# 
# Explanation:
# Node 1's value is 1, both of its next and random pointer points to Node 2.
# Node 2's value is 2, its next pointer points to null and its random pointer
# points to itself.
# 
# 
# 
# 
# Note:
# 
# 
# You must return the copy of the given head as a reference to the cloned list.
# 
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

        
## My: using random to point to the copy  1
## Isn't a good solution, not as good as hashmap because you modified the former linkedlist
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        cur = head
        dummyhead = Node(0,0,0)
        curcopy = dummyhead
        while cur:
            curcopy.next = Node(cur.val,cur.next,cur.random)
            curcopy = curcopy.next
            cur.random = curcopy
            cur = cur.next
        curcopy.next = None
        curcopy = dummyhead.next
        while curcopy:
            if curcopy.random:
                curcopy.random = curcopy.random.random
            curcopy = curcopy.next
        return dummyhead.next
## My: using random to point to the copy 2
## Isn't a good solution, not as good as hashmap because you modified the former linkedlist

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        cur = head
        while cur:
            cur.random = Node(cur.val,cur.next,cur.random)
            cur = cur.next
        cur = head
        while cur:
            if cur.random.next:
                cur.random.next = cur.random.next.random
            if cur.random.random:
                cur.random.random = cur.random.random.random
            cur = cur.next
        return head.random

## Buildin
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        from copy import deepcopy
        return deepcopy(head)

## Fastest solution from discussion using dictionary
# My hash map solution
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        cur = head
        dct = {}
        while cur:
            dct[cur] = Node(cur.val,cur.next,cur.random)
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                dct[cur].next = dct[cur.next]
            if cur.random:
                dct[cur].random = dct[cur.random]
            cur=cur.next
        return dct[head]
       

#### Graph BFS 看懂了，和dict差不多， DFS的没看懂
###https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43679/A-nice-and-easy-Python-DFS-solution-with-explanation
##DFS

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # Use DFS at first
        self.visited = collections.defaultdict(RandomListNode)
        return self.DFS(head)
        
    def DFS(self, head):
        if not head:
            return None
        if head not in self.visited:
            newHead = RandomListNode(head.label) # newHead
            self.visited[head] = newHead
            newHead.next = self.DFS(head.next) # visit next branch
            newHead.random = self.DFS(head.random) # visite random branch
            return newHead
        else:
            return self.visited[head] # o/w return the refered as newHead
##BFS

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # Try BFS this time
        # assume all node in queue have been copied before putting into the queue
        if not head: return None
        newHead = RandomListNode(head.label)
        visited = {head:newHead}
        queue = collections.deque([head])
        nextQ = collections.deque([])
        while queue:
            node = queue.popleft()
            newNode = visited[node] # creat new Node
            # next branch
            if node.next and node.next not in visited:
                newNext = RandomListNode(node.next.label)
                visited[node.next] = newNext
                newNode.next = newNext
                nextQ.append(node.next)
            elif node.next: # check not None
                newNode.next = visited[node.next] # connect copy
            # random branch
            if node.random and node.random not in visited:
                newRan = RandomListNode(node.random.label)
                visited[node.random] = newRan
                newNode.random = newRan
                nextQ.append(node.random)
            elif node.random: # check not None
                newNode.random = visited[node.random] 
            if not queue:
                queue, nextQ = nextQ, queue # swap
        return newHead
## Without using dictionary 
#http://www.cnblogs.com/zuoyuan/p/3745126.html
#https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43689/Python-solution-without-using-dictionary.
#https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43587/Clear-O(n)-complexity-with-O(1)-space-in-Python

## Without using dictionary: Clear 3 steps
class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:return None
        self.copyNext(head)
        self.copyRandom(head)
        return splitList(head)

        
    def copyNext(self,head):
        while head:
            newNode = RandomListNode(head.label)
            newNode.random = head.random
            newNode.next = head.next
            head.next = newNode
            head = head.next.next

    def copyRandom(self,head):
        while head:
            if head.next.random:
                head.next.random = head.random.next
            head = head.next.next 

    def splitList(self,head):
        newHead = head.next
        while head:
            tmp = head.next
            head.next = tmp.next
            head = head.next
            if tmp.next:
                tmp.next = tmp.next.next
        return newHead
## Without using dictionary: whole one
def copyRandomList(self, head):
    if not head:
        return None
    p = head
    while p:
        node = RandomListNode(p.label)
        node.next = p.next
        p.next = node
        p = p.next.next
        # p = node.next
    p = head    
    while p:
        if p.random:
            p.next.random = p.random.next
        p = p.next.next
    newhead = head.next
    pold = head
    pnew = newhead
    while pnew.next:
        pold.next = pnew.next
        pold = pold.next
        pnew.next = pold.next
        pnew = pnew.next
    pold.next = None
    pnew.next = None
    return newhead