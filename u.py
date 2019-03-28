# class Solution:
#     def findKthLargest(self, nums, k: int) -> int:
#         ## use quickSelect; can also use heap
#         return self.quickSelect(nums,k)
    
#     def quickSelect(self, nums, k):
#         idx = self.partition(nums)
#         print(idx)
#         if idx+1 == k:
#             return nums[idx]
#         elif idx+1 < k:
#             return self.quickSelect(nums[idx+1:], k-idx-1)
#         else:  # idx+1 > k
#             return self.quickSelect(nums[:idx], k)
        
#     def partition(self, nums):
#         print("partition",nums)
#         pivot = nums[-1]  # counte comparison
#         idx = 0  # processed index
#         for i in range(0,len(nums)-1):
#             if nums[i]> pivot:  # bigger left
#                 nums[idx], nums[i] = nums[i], nums[idx]
#                 idx += 1
#         nums[idx], nums[-1] = nums[-1], nums[idx]
#         return idx

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

        

s=Solution()
print(s.findKthLargest([1,4,3,2,5,6,9,8],4))        