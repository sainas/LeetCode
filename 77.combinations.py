#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (46.25%)
# Total Accepted:    189.1K
# Total Submissions: 408.1K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
# 
# Example:
# 
# 
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 
#

## Recursion
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == n:
            return [[x for x in range(1,n+1)]] 
        if k == 1:
            return list(map(lambda x: [x],range(1,n+1)))
        lst = []
        lst+=list(map(lambda x: x,self.combine(n-1,k)))
        lst+=list(map(lambda x: x+[n],self.combine(n-1,k-1)))
        return lst

## Recursion: clean code using list comprehension
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == n:
            return [[x for x in range(1,n+1)]] 
        if k == 1:
            return [[x] for x in range(1,n+1)]
        return self.combine(n-1,k) +[x + [n] for x in self.combine(n-1,k-1)]



## 另一种Recursion: DFS
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.dfs(n, k, 0, [], res)
        return res

    def dfs(self, n, k, index, path, res):
        #if k < 0:  #backtracking
            #return 
        if k == 0:
            res.append(path)
            return # backtracking 
        for i in range(index, n):
            self.dfs(n, k-1, i+1, path+[i+1], res)

