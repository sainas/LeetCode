#
# @lc app=leetcode id=980 lang=python3
#
# [980] Unique Paths III
#
# https://leetcode.com/problems/unique-paths-iii/description/
#
# algorithms
# Hard (72.97%)
# Total Accepted:    5.8K
# Total Submissions: 8.1K
# Testcase Example:  '[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]'
#
# On a 2-dimensional grid, there are 4 types of squares:
# 
# 
# 1 represents the starting square.  There is exactly one starting square.
# 2 represents the ending square.  There is exactly one ending square.
# 0 represents empty squares we can walk over.
# -1 represents obstacles that we cannot walk over.
# 
# 
# Return the number of 4-directional walks from the starting square to the
# ending square, that walk over every non-obstacle square exactly once.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
# 
# 
# Example 2:
# 
# 
# Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths: 
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
# 
# 
# Example 3:
# 
# 
# Input: [[0,1],[2,0]]
# Output: 0
# Explanation: 
# There is no path that walks over every empty square exactly once.
# Note that the starting and ending square can be anywhere in the grid.
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= grid.length * grid[0].length <= 20
# 
#
# 

### first submit: bfs     O(4^(RC))    
class Solution:
    def uniquePathsIII(self, grid) -> int:
        self.numpath = 0
        numzero = 0
        self.row=len(grid)
        self.col=len(grid[0])
        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j]==1:
                    startx=i
                    starty=j
                if grid[i][j]==0:
                    numzero+=1
                if grid[i][j]==2:
                    self.end=(i,j)
        self.pathnum(grid,startx,starty,numzero+1)        
        return self.numpath
    def pathnum(self,grid,x,y,zero):
            if grid[x][y]<0:return
            if grid[x][y]==2:
                if zero == 0:
                    self.numpath += 1
                return
            grid[x][y]=-1
            for i,j in self.neighbor(x,y,self.row,self.col):
                self.pathnum(grid,i,j,zero-1)
            grid[x][y]=0
            ## must change back
            ## because Python can not pass by value, only pass by referance
            ## if C++, can pass by value and no need to change back(but space complexity 
            ## would be high)

    def neighbor(self,x,y,row,col):
        lst=[]
        for i,j in [[0,1],[0,-1],[1,0],[-1,0]]:
            a,b = x+i,y+j
            if a>=0 and a<row and b>=0 and b<col:
                lst.append([a,b])
        return lst
        
## MY DP  O(R∗C∗2^(RC))
class Solution:
    def uniquePathsIII(self, grid) -> int:
        self.numpath = 0
        s=set()
        numzero = 0
        self.row=len(grid)
        self.col=len(grid[0])
        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j]==1:
                    startx=i
                    starty=j
                if grid[i][j]==0:
                    s.add((i,j))
                    numzero+=0
        self.dfs(grid,startx,starty,s,numzero)
        return self.numpath
    def dfs(self,grid,x,y,s,numzero):
        if not s:
            for i,j in self.neighbor(x,y) :
                if grid[i][j]==2:
                    self.numpath+=1
            return
        for i,j in self.neighbor(x,y) :
            if (i,j) in s:
                s.remove((i,j))
                self.dfs(grid,i,j,s,numzero-1)
                s.add((i,j))
            
    def neighbor(self,x,y):
        lst=[]
        for i,j in [[0,1],[0,-1],[1,0],[-1,0]]:
            a,b = x+i,y+j
            if a>=0 and a<self.row and b>=0 and b<self.col:
                lst.append([a,b])
        return lst
           
## A more clear dfs
## https://leetcode.com/problems/unique-paths-iii/discuss/221946/JavaPython-Brute-Force-Backstracking
class Solution:
    def uniquePathsIII(self, A):
        self.res = 0
        m, n,empty = len(A), len(A[0]),1
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1: x,y = (i, j)
                elif A[i][j] == 2: end = (i, j)
                elif A[i][j] == 0: empty += 1
        def dfs(x, y, empty):
            if not (0 <= x < m and 0 <= y < n and A[x][y] >= 0): return
            if (x, y) == end:
                self.res += empty == 0
                return
            A[x][y] = -2
            dfs(x + 1, y, empty - 1)
            dfs(x - 1, y, empty - 1)
            dfs(x, y + 1, empty - 1)
            dfs(x, y - 1, empty - 1)
            A[x][y] = 0
        dfs(x,y, empty)
        return self.res

s=Solution()
print(s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])) 

