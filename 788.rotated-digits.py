#
# @lc app=leetcode id=788 lang=python3
#
# [788] Rotated Digits
#
# https://leetcode.com/problems/rotated-digits/description/
#
# algorithms
# Easy (53.30%)
# Total Accepted:    23.4K
# Total Submissions: 43.8K
# Testcase Example:  '10'
#
# X is a good number if after rotating each digit individually by 180 degrees,
# we get a valid number that is different from X.  Each digit must be rotated -
# we cannot choose to leave it alone.
# 
# A number is valid if each digit remains a digit after rotation. 0, 1, and 8
# rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each
# other, and the rest of the numbers do not rotate to any other number and
# become invalid.
# 
# Now given a positive number N, how many numbers X from 1 to N are good?
# 
# 
# Example:
# Input: 10
# Output: 4
# Explanation: 
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after
# rotating.
# 
# 
# Note:
# 
# 
# N  will be in range [1, 10000].
# 
# 
#


# ## 仿照1015 mask那个方法写的：算出[0,1,2,5,6,8,9]组合，减去只有[0,1,8]的组合数
# class Solution:
#     def rotatedDigits(self, N: int) -> int:
#         self.count = 0
#         self.myset =  [0,1,2,5,6,8,9]
#         def dfs(n):
#             if n > N: return
#             self.count +=1
#             for i in self.myset:
#                 dfs(n*10+i)
        
#         for i in self.myset:
#             if i:
#                 dfs(i)
#         savecount = self.count
#         self.count = 0
#         self.myset =  [0,1,8]
#         for i in self.myset:
#             if i:
#                 dfs(i)
#         return savecount - self.count
                    
## 仿照1015另一种方法写的
class Solution:
    def rotatedDigits(self, N: int) -> int:
        def helper(lst, myset):
            ans = 0
            for i in range(1,len(lst)):
                ans += (len(myset)-1)*pow(len(myset),i-1)
            for i,x in enumerate(lst):
                for y in myset:
                    if i|y and y<x:
                        ans += pow(len(myset),len(lst)-i-1)
                if x not in myset:
                    break
            return ans
        lst = list(map(int,str(N+1)))   
        myset1 = [0,1,2,5,6,8,9]
        myset2 = [0,1,8]
        return helper(lst,myset1)-helper(lst,myset2)

## Traversal
class Solution:
    def rotatedDigits(self, N: int) -> int:
        count =  0
        for i in range(2,N+1):
            s = str(i)
            if '3' in s or '4' in s or '7' in s:
                continue
            if '2' in s or '5' in s or '6' in s or '9' in s:
                count +=1
        return count

s=Solution()
print(s.rotatedDigits(20))
