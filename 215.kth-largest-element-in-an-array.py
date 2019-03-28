#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (46.29%)
# Total Accepted:    340.8K
# Total Submissions: 732K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# Example 1:
# 
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
#


## Quickselect O(n)
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        ## use quickSelect; can also use heap
        return self.quickSelect(nums,0,len(nums)-1,k)
    
    def quickSelect(self, nums, start, end, k):
        idx = self.partition(nums,start, end)
        if idx+1 == k:
            return nums[idx]
        elif idx+1 < k:
            return self.quickSelect(nums,idx+1,end,k)
        else:  # idx+1 > k
            return self.quickSelect(nums,start,idx-1,k)
        
    def partition(self, nums,start, end):
        pivot = nums[end]  # counte comparison
        idx = start  # processed index
        for i in range(start,end):
            if nums[i]> pivot:  # bigger left
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
        nums[idx], nums[end] = nums[end], nums[idx]
        return idx    

## Max Heap 1
class Solution(object):
    def findKthLargest(self, nums, k):
        from heapq import heapify,heappop
        heapify(nums)
        for _ in range(len(nums)-k+1):
            value =  heappop(nums)
        return value

## Max Heap 2
class Solution(object):
    def findKthLargest(self, nums, k):
        from heapq import heapify,heappop
        nums = [-i for i in nums]
        heapify(nums)
        for _ in range(k):
            value =  heappop(nums)
        return -value

## Min Heap 1
class Solution(object):
    def findKthLargest(self, nums, k):
        import heapq
        minheap= nums[:k]
        heapq.heapify(minheap)
        for num in nums[k:]:
            if num> minheap[0]:
                heapq.heappop(minheap)
                heapq.heappush(minheap,num)
        return minheap[0]

## Min Heap 2
class Solution(object):
    def findKthLargest(self, nums, k):
        import heapq
        return heapq.nlargest(k, nums)[-1]
