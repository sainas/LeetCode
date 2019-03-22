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

## havn't go through
# Bit Manipulation    
def subsets2(self, nums):
    res = []
    nums.sort()
    for i in xrange(1<<len(nums)):
        tmp = []
        for j in xrange(len(nums)):
            if i & 1 << j:  # if i >> j & 1:
                tmp.append(nums[j])
        res.append(tmp)
    return res


def subsets(self, nums):
    return [[nums[i] for i in range(len(nums)) if mask >> i & 1]
            for mask in range(2 ** len(nums))]

def subsets(self, nums):
    return [filter(None, l) for l in itertools.product(*zip(nums, [None] * len(nums)))]
