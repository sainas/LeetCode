# #
# # @lc app=leetcode id=95 lang=python3
# #
# # [95] Unique Binary Search Trees II
# #
# # https://leetcode.com/problems/unique-binary-search-trees-ii/description/
# #
# # algorithms
# # Medium (34.86%)
# # Total Accepted:    129.4K
# # Total Submissions: 371.1K
# # Testcase Example:  '3'
# #
# # Given an integer n, generate all structurally unique BST's (binary search
# # trees) that store values 1 ... n.
# # 
# # Example:
# # 
# # 
# # Input: 3
# # Output:
# # [
# # [1,null,3,2],
# # [3,2,null,1],
# # [3,1,null,null,2],
# # [2,1,3],
# # [1,null,2,null,3]
# # ]
# # Explanation:
# # The above output corresponds to the 5 unique BST's shown below:
# # 
# # ⁠  1         3     3      2      1
# # ⁠   \       /     /      / \      \
# # ⁠    3     2     1      1   3      2
# # ⁠   /     /       \                 \
# # ⁠  2     1         2                 3
# # 
# # 
# #
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# ## Dynamic Programming
# ## 我写的超慢版本
# class Solution:
#     cache={}
#     def generateTrees(self, n: int) :
#         from copy import deepcopy
#         if n ==1:
#             return [TreeNode(1)]
#         if n ==0:
#             return []
#         dp=[[]]*(n+1)
#         dp[0]= [None]
#         dp[1]=[TreeNode(1)]
#         dp2=[[]]*(n+1)
#         dp2[0]= [None]
#         dp2[1]= [1]
        
#         for i in range(2,n+1):
#             for j in range(i):
#                 for k1 in dp[j]:
#                     for k2 in dp[i-j-1]:
#                         Tree = TreeNode(j+1)
#                         Tree.left = k1
#                         if not k2:
#                             Tree.right = k2
#                         else:
#                             copytree = deepcopy(k2)
#                             self.generatenewtree(copytree,j+1)
#                             Tree.right = copytree
#                         dp[i]=dp[i]+[Tree]
#                         dp2[i]=dp2[i]+[j+1]
#         return dp[n]

#     def generatenewtree(self,tree,n):
#         if tree:
#             tree.val +=n
#             self.generatenewtree(tree.left,n)
#             self.generatenewtree(tree.right,n)

# ## 网上找的更清晰的，原理是一样     
# class Solution(object):
#     def generateTrees(self, n):
#         """
#         :type n: int
#         :rtype: List[TreeNode]
#         """
#         if n == 0:
#             return []
        
#         res = [[None]]
        
#         # left_tree_res*right_tree_res
#         # dp[1] = dp[0]*dp[0](root:1)
#         # dp[2] = dp[0]*dp[1](root:1) + dp[1]*dp[0](root:2)
#         # dp[3] = dp[0]*dp[2](root:1) + dp[1]*dp[1](root:2) + dp[2]*dp[0](root:3)
#         # dp[k] = dp[0]*dp[k-1](root:1) + ... dp[i]*dp[k-1-i](root:i+1) + ... dp[k-1]*dp[0](root:k)
#         for x in range(1, n+1):
#             res.append([])
#             for i in range(0, x):
#                 left_set = res[i]
#                 right_set = res[x-1-i]
#                 for left in left_set:
#                     for right in right_set:
#                         # root value will always be i+1
#                         root = TreeNode(i+1)
#                         # left tree no need to adjust anything since it's a UBST of 1 to i
#                         root.left = left
#                         # right tree need to add i+1 to all nodes
#                         root.right = copy_tree(right, i+1)
#                         res[x].append(root)
#         return res[n]

# # Helper function to copy a tree and append same value to all nodes
# def copy_tree(node, val):
#     if node is None:
#         return None
#     root = TreeNode(node.val + val)
#     if node.left is not None:
#         root.left = copy_tree(node.left, val)
#     if node.right is not None:
#         root.right = copy_tree(node.right, val)
#     return root

# ## DP 可以用一个参数+一个generate function，或者用两个参数

# ## recursion
# class Solution(object):
#     def generateTrees(self, n):
#         """
#         :type n: int
#         :rtype: List[TreeNode]
#         """
#         if n == 0:
#             return [[]]
#         return self.dfs(1, n+1)
        
#     def dfs(self, start, end):
#         if start == end:
#             return None
#         result = []
#         for i in range(start, end):
#             for l in self.dfs(start, i) or [None]:
#                 for r in self.dfs(i+1, end) or [None]:
#                     node = TreeNode(i)
#                     node.left, node.right  = l, r
#                     result.append(node)
#         return result

## 网上的一个解法 用yield
class Solution:
    # @return a list of tree node
    # 2:30
    import copy
    def generateTrees(self, n):
        nodes = list(map(TreeNode, range(1, n+1)))
        return list(map(copy.deepcopy, self.buildTree(nodes)))

    def buildTree(self, nodes):
        n = len(nodes)
        if n == 0:
            yield None
            return
        for i in range(n):
            root = nodes[i]
            for left in self.buildTree(nodes[:i]):
                for right in self.buildTree(nodes[i+1:]):
                    root.left, root.right = left, right
                    yield root




# s=Solution()
# print(s.generateTrees(3).val)
        

