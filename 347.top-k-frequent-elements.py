#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (53.26%)
# Total Accepted:    177K
# Total Submissions: 331.1K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given a non-empty array of integers, return the k most frequent elements.
# 
# Example 1:
# 
# 
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Note: 
# 
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is
# the array's size.
# 
# 
#

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         from collections import Counter
#         return [list1[0] for list1 in Counter(nums).most_common(k)]

# Using QuickSelect Average O(n)
# QuickSort is O(nlog(n))
# This code: every time creat a new sublist
#Reference:https://leetcode.com/problems/top-k-frequent-elements/discuss/250326/Python-O(n)-with-quickSelect
class Solution:
    def topKFrequent(self, nums: int, k: int):
        ## use quickSelect; can also use heap
        dict1 = {}  # num : counter
        for key in nums:
            dict1[key] = dict1.get(key,0) + 1
        # conver to a list
        lst1 = list(dict1.items())
        return self.quickSelect(lst1,k)
    
    def quickSelect(self, nums, k):
        idx = self.partition(nums)
        if idx+1 == k:
            return [x[0] for x in nums[:idx+1]]
        elif idx+1 < k:
            return [x[0] for x in nums[:idx+1]] + self.quickSelect(nums[idx+1:], k-idx-1)
        else:  # idx+1 > k
            return self.quickSelect(nums[:idx], k)
        
    def partition(self, nums):
        pivot = nums[-1][1]  # counte comparison
        idx = 0  # processed index
        for i in range(len(nums)-1):
            if nums[i][1] > pivot:  # bigger left
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
        nums[idx], nums[-1] = nums[-1], nums[idx]
        return idx

# Better:Using QuickSelect Average O(n), no slicing (no new list)
# QuickSort is O(nlog(n))
# Haven't write, just replace the slicing with two variable: "start" and "end"

