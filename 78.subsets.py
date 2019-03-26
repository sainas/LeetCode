#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (51.29%)
# Total Accepted:    338.8K
# Total Submissions: 659K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#
## 3-lines python
##https://leetcode.com/problems/subsets/discuss/240531/Python-3-line-Easy-Recursion
class Solution:
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        if not nums: return [[]]
        prefix = self.subsets(nums[:-1])
        return prefix + [pre + [nums[-1]] for pre in prefix]


## 1-line python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [[]] if len(nums)==0 else [i+j for i in self.subsets(nums[1:]) for j in [[], [nums[0]]]]


## My First Try
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        lst = self.subsets(nums[:-1])
        lst += list(map(lambda x: x+[nums[-1]],lst))
        return lst

## An amazing list comprehension
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            result += [ x + [num] for x in result]
        return result

## Following: Using reduce to replace the loop to make it shorter
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from functools import reduce
        return reduce(lambda subsets, n: subsets + [s+[n] for s in subsets], nums, [[]])

## Bit manipulation
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import compress
        ans = []
        for x in range(pow(2,len(nums))):
            ans.append(list(compress(nums,[int(i) for i in (bin(x)[2:].zfill(len(nums)))])))
        return ans

## Another bit manipulation without compress
class Solution:
    def subsets(self, nums):
        res = []
        nums.sort()
        for i in range(1<<len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i & 1 << j:  # if i >> j & 1: (both works)
                    tmp.append(nums[j])
            res.append(tmp)
        return res


## Another bit manipulation
class Solution:
    def subsets(self, nums):
        return [[nums[i] for i in range(len(nums)) if mask >> i & 1]
            for mask in range(1<<len(nums))]

## One-line bit manipulation using map
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import compress
        return list(map(lambda x: list(compress(nums,[int(i) for i in (bin(x)[2:].zfill(len(nums)))])),range(pow(2,len(nums)))))

## DFS
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(index,path):
            ans.append(path)
            for i in range(index, len(nums)):
                dfs(i+1, path+[nums[i]])
        dfs(0,[])
        return ans

## Using combinations from the library:
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [s for n in range(len(nums)+1)
                for s in itertools.combinations(nums, n)]

## Cartesian product: itertools.product
class Solution:
    def subsets(self, nums):
        return [list(filter(lambda x: x != None, l)) for l in itertools.product(*zip(nums, [None] * len(nums)))]

## Using both product and compress
from itertools import product,compress
class Solution(object):
    def subsets(self, nums):
        results = []
        for i in product([0,1],repeat = len(nums)):
            results.append(list(compress(nums,i)))
        return results

## Another binary mask with Cartesian product
from itertools import product
class Solution(object):
    def subsets(self, nums):
        mask = product((0, 1), repeat=len(nums))
        return [[nums[i] for i, on in enumerate(j) if on] for j in mask]