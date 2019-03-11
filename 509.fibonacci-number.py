#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#
# https://leetcode.com/problems/fibonacci-number/description/
#
# algorithms
# Easy (66.55%)
# Total Accepted:    26.6K
# Total Submissions: 40K
# Testcase Example:  '2'
#
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the
# Fibonacci sequence, such that each number is the sum of the two preceding
# ones, starting from 0 and 1. That is,
# 
# 
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.
# 
# 
# Given N, calculate F(N).
# 
# 
# 
# Example 1:
# 
# 
# Input: 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# 
# 
# Example 2:
# 
# 
# Input: 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# 
# 
# Example 3:
# 
# 
# Input: 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
# 
# 
# 
# 
# Note:
# 
# 0 ≤ N ≤ 30.
# 
#

## recursion
# class Solution:
#     def fib(self, N: int) -> int:
#         if N <2:
#             return N
#         else:
#             return self.fib(N-1)+self.fib(N-2)

## cache recursion   
# class Solution:
#     cache={}
#     def fib(self, N: int) -> int:
#         if N in self.cache:
#             return self.cache[N]
#         else:
#             if N <2:
#                 self.cache[N] = N
#                 return self.cache[N]
#             else:
#                 self.cache[N] = self.fib(N-1)+self.fib(N-2)
#                 return self.cache[N]

## tail recursion

class Solution:
    def fib(self, N: int) -> int:
        if N<2:
            return N
        else:
            def tail_fib(first, second, N):
                if N == 2:
                    return first + second
                else: 
                    return tail_fib(second, first+second,N-1)
            return tail_fib(0, 1, N)

        
        



## iteration
# class Solution:
#     def fib(self, N: int) -> int:
#         if N<2:
#             return N
#         else:
#             cur1 = 0
#             cur2 = 1
#             for _ in range(N-1):
#                 cur3 = cur1+cur2
#                 cur1 = cur2
#                 cur2 = cur3
#             return cur3


## Test
# s=Solution()
# print(s.fib(6))
