#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (27.58%)
# Total Accepted:    293.7K
# Total Submissions: 1.1M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (x^n).
# 
# Example 1:
# 
# 
# Input: 2.00000, 10
# Output: 1024.00000
# 
# 
# Example 2:
# 
# 
# Input: 2.10000, 3
# Output: 9.26100
# 
# 
# Example 3:
# 
# 
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 
# Note:
# 
# 
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
# 
# 

## Recursion

# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n ==0:
#             return 1
#         elif n == 1:
#             return x
#         elif n <0:
#             return self.myPow(1/x,-n)
#         else:
#             return self.myPow(x*x,int(n/2))*(x if n%2 else 1)        

##
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n ==0:
#             return 1
#         elif n <0:
#             return 1/self.myPow(x,-n)
#         else:
#             result = 1
#             powern = x
#             for i in bin(n)[::-1]:
#                 if i == 'b':
#                     return result
#                 elif i == '1':
#                     result *= powern
#                 powern *= powern

##
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n

# s=Solution()
# print(s.myPow(8.84372,-5)-pow(8.84372,-5))
# print(s.myPow(-2,5))
# print((-2)**5)
# print(s.myPow(2,5))
# print(s.myPow(8.84372,-5))
# # # # print(list(map(lambda x:s.myPow(8.84372, -x)-pow(8.84372, -x),range(10))))
