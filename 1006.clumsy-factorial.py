#
# @lc app=leetcode id=1006 lang=python3
#
# [1006] Clumsy Factorial
#
# https://leetcode.com/problems/clumsy-factorial/description/
#
# algorithms
# Medium (55.22%)
# Total Accepted:    4.8K
# Total Submissions: 8.6K
# Testcase Example:  '4'
#
# Normally, the factorial of a positive integer n is the product of all
# positive integers less than or equal to n.  For example, factorial(10) = 10 *
# 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.
# 
# We instead make a clumsy factorial: using the integers in decreasing order,
# we swap out the multiply operations for a fixed rotation of operations:
# multiply (*), divide (/), add (+) and subtract (-) in this order.
# 
# For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.  However,
# these operations are still applied using the usual order of operations of
# arithmetic: we do all multiplication and division steps before any addition
# or subtraction steps, and multiplication and division steps are processed
# left to right.
# 
# Additionally, the division that we use is floor division such that 10 * 9 / 8
# equals 11.  This guarantees the result is an integer.
# 
# Implement the clumsy function as defined above: given an integer N, it
# returns the clumsy factorial of N.
# 
# 
# 
# Example 1:
# 
# 
# Input: 4
# Output: 7
# Explanation: 7 = 4 * 3 / 2 + 1
# 
# 
# Example 2:
# 
# 
# Input: 10
# Output: 12
# Explanation: 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 10000
# -2^31 <= answer <= 2^31 - 1  (The answer is guaranteed to fit within a 32-bit
# integer.)
# 
# 
#
class Solution:
    def clumsy(self, N: int) -> int:
        result = 0
        n = N
        while(N>0):
            minus = 0
            if N == n:
                minus = 1
            if N >=4:
                result -= int(N*(N-1)/(N-2))-(N-3)
                N = N-4
            elif N ==3:
                result -=int( N*(N-1)/(N-2))
                N = N-3
            elif N ==2:
                result -= N*(N-1)
                N=N-2
            elif N ==1:
                result -= N
                N=N-1 
            result = result*(-1)*minus
        return result 

## Recursion
class Solution:
    def clumsy(self, N: int) -> int:
        def caltail(n):
            if n == 1: return -1
            if n == 2: return -2
            if n == 3: return -6
            if n == 4: return -5
            return caltail(n - 4) - n * (n - 1) // (n - 2) + (n - 3)
        
        if N == 1: return 1
        if N == 2: return 2
        if N == 3: return 6
        if N == 4: return 7
        return N * (N - 1) // (N - 2) + N - 3 + caltail(N - 4)
## Test             
S=Solution()
print(S.clumsy(10))

