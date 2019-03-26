#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (46.60%)
# Total Accepted:    268.2K
# Total Submissions: 573.6K
# Testcase Example:  '3\n2'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# How many possible unique paths are there?
# 
# 
# Above is a 7 x 3 grid. How many possible unique paths are there?
# 
# Note: m and n will be at most 100.
# 
# Example 1:
# 
# 
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the
# bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# 
# 
# Example 2:
# 
# 
# Input: m = 7, n = 3
# Output: 28
# 
### Recursion: Time Limit Exceeded	
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1)

## DP
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        DP = {}
        DP[(1,1)]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i ==1 or j ==1:
                    DP[(i,j)]=1
                else:
                    DP[(i,j)] = DP[(i-1,j)]+DP[(i,j-1)]
        return DP[(m,n)]
        
## Math
class Solution:
    from functools import reduce
    def uniquePaths(self, m: int, n: int) -> int:
        if m ==1 or n ==1:
            return 1
        return self.combination(m+n-2,m-1)
    def combination(self,m,n):
        from functools import reduce
        a = reduce(lambda x,y: x*y,range(m-n+1,m+1))
        b = reduce(lambda x,y: x*y,range(1,n+1))
        return int(a/b)
        
