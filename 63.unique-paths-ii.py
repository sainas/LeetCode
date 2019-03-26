#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (33.24%)
# Total Accepted:    188.4K
# Total Submissions: 566.5K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?
# 
# 
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# Note: m and n will be at most 100.
# 
# Example 1:
# 
# 
# Input:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# 
# 
#

## Inplace
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1]==1:
            return 0
        obstacleGrid[0][0] = -1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if not obstacleGrid[i][j]:
                    if j:
                        if obstacleGrid[i][j-1]!=1:
                            obstacleGrid[i][j]+=obstacleGrid[i][j-1]
                    if i:
                        if obstacleGrid[i-1][j]!=1:
                            obstacleGrid[i][j]+=obstacleGrid[i-1][j]
                           
        return -obstacleGrid[-1][-1]

## DP        
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1]==1:
            return 0
        dp= [[0 for x in range(len(obstacleGrid[0]))] for y in range(len(obstacleGrid))] 
        dp[0][0]=1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i:
                    dp[i][j]+=dp[i-1][j]
                if j:
                    dp[i][j]+=dp[i][j-1]
                dp[i][j]*=(1-obstacleGrid[i][j])
        return dp[-1][-1]       

