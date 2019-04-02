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
    def numEnclaves(self, A):
        def sink(i, j):
            if 0 <= i < len(A) and 0 <= j < len(A[0]) and A[i][j] == 1:
                A[i][j] = 0
                print(A,i,j)
                # sink(i+1,j)
                # sink(i-1,j)
                # sink(i,j+1)
                # sink(i,j-1)
                # list(map(lambda x,y:sink(x,y), [i+1, i-1, i, i], [j, j, j+1, j-1]))
                list(map(sink, [i+1, i-1, i, i], [j, j, j+1, j-1]))
                return 1
            return 0
        # for i in range(len(A)):
        #     sink(i,0)
        #     sink(i,len(A[0])-1)
        # for j in range(len(A[0])):
        #     sink(0,j)
        #     sink(len(A)-1,j)
        list(map(lambda x:sink(x,0),[i for i in range(len(A))]))
        list(map(sink,[0,len(A)-1],[j for j in range(len(A[0]))]))
        print('qq',A)
        return sum( sink(i,j) for i in range(len(A)) for j in range(len(A[0])))
        

s=Solution()
a=[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]] 
b=[[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]  
print(s.numEnclaves(a ))   
print(s.numEnclaves(b ))   
  