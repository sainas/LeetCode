#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (40.48%)
# Total Accepted:    313.8K
# Total Submissions: 774.2K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 
# 
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
# 
#

### 我自己写的labeling的一种方法，先全都label，并且把连起来的区域放在一个set里面
### 比dfs要快
# class Solution:
#     def numIslands(self, grid ) -> int:
#         label=0
#         num=0
#         lst = []
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':
#                     if (i ==0 or grid[i-1][j]=='0') and (j==0 or grid[i][j-1]=='0'):
#                         label += 1
#                         grid[i][j] =label
#                     elif i ==0 or grid[i-1][j]=='0':
#                         grid[i][j] = grid[i][j-1]
#                     elif j==0 or grid[i][j-1]=='0':
#                         grid[i][j] = grid[i-1][j]
#                     else:
#                         grid[i][j] = grid[i][j-1]
#                         set1 = -1
#                         set2 = -1
#                         for k in range(len(lst)):
#                             if grid[i-1][j] in lst[k]:
#                                 set1 = k
#                             elif grid[i][j-1] in lst[k]:
#                                 set2 = k
#                         if set1 == -1 and set2 ==-1:
#                             lst.append(set([grid[i-1][j],grid[i][j-1]]))
#                         elif set1 == -1:
#                             lst[set2].add(grid[i-1][j])
#                         elif set2 == -1:
#                             lst[set1].add(grid[i][j-1])
#                         elif set1!=set2:
#                             lst[set1]=lst[set1]|lst[set2]
#                             lst.pop(set2)
                                
#         num = 0
#         for sets in lst:
#             if sets:
#                 num += len(sets)-1
#         return  label - num

### dfs的写法
class Solution:
    def numIslands(self, grid ) -> int:
        def dfs(i,j):
            if i>=0 and i<len(grid) and j>=0 and j<len(grid[0]):
                if grid[i][j] =='1':
                    grid[i][j]='$'
                    dfs(i-1,j) 
                    dfs(i,j-1)
                    dfs(i+1,j)
                    dfs(i,j+1)
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] =='1':
                    num+=1
                    dfs(i,j)
        return num
        
### dfs 简洁的写法
### https://leetcode.com/problems/number-of-islands/discuss/56349/7-lines-Python-~14-lines-Java
def numIslands(self, grid):
    def sink(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
            grid[i][j] = '0'
            list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)))
            return 1
        return 0
    return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))    

s=Solution()
result = s.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
print(result)