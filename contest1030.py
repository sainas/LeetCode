class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return []
        dct = {}
        stack = []
        lst = []
        index = 0
        while head:
            if not stack or stack[-1][1]>=head.val:
                stack.append((index,head.val))
                head = head.next
                lst.append(0)
                index +=1
            else:
                idx,value = stack.pop()
                lst[idx] = head.val
                continue
        return lst
                
        