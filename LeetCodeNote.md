# LeetCodeNote
## **347 ** 

用QuickSelect重新做了一遍。关键是python的浅复制修改的还是原变量，所以list如果传入某个函数，然后在函数里修改了以后并不需要return了直接就在原地改了！
## Given an array of integers, find the median of the array.  What is the time complexity?  Can you do this in O(N) complexity?
QuickSelect

## How would you compute the running median of a stream of integers? 
一个小顶堆一个大顶堆
## Algorithm
### 如何用stack实现queue
三种方法
思路一：

我们设定s1是入栈的，s2是出栈的。



入队列，直接压到s1即可



出队列，先把s1中的元素倒入到s2中，弹出s2中的栈顶元素；再把s2的剩余元素全部倒回s1中。


缺点：

每次只要出栈一个元素就要将元素倒来倒去，麻烦！！！




思路2：

入队列时：
如果s1为空，把s2中所有的元素倒出压到s1中。否则直接压入s1   

出队列时：
如果s2不为空，把s2中的栈顶元素直接弹出。否则，把s1的所有元素全部弹出压入s2中，再弹出s2的栈顶元素



wKiom1cMppLwMd0QAAB3LagChFk387.png





思路1无条件地每次都要将元素倒来倒去，思路2出队时较思路1简单




思路3：

我们设定s1是入栈的，s2是出栈的

入队列：直接压入元素至s1即可

出队列：如果s2不为空，把s2中的栈顶元素直接弹出。否则，把s1的所有元素全部弹出压入s2中，再弹出s2的栈顶元素



wKioL1cMp8HR1m6aAABLlSxXUHE848.png



相比于方法2，入队直接压入即可~
###
### 学习map reduce filter lambda
下面是两个综合利用以上四个函数的例子：
* 例子1：计算5!+4!+3!+2!+1!
```
a=[5,4,3,2,1]
def fun(x):
    result = 1    
    while x >= 1:
        result = result * x
        x = x - 1
    return result
print reduce(lambda x,y:x+y, map(fun,a))
```
* 例子2：将100以内的质数挑选出来
```
import math

def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print(list(filter(isPrime,range(1,100))))
```
---------------------
作者：Zhu_Julian 
来源：CSDN 
原文：https://blog.csdn.net/dbanote/article/details/8912250 
版权声明：本文为博主原创文章，转载请附上博文链接！
## Data Structure
### Complexity

![img](LeetCodeNote.assets/screen-shot-2018-04-28-at-174531.png)



### Tree

#### Traversal
##### DFS
###### Recursion
Tree Traversals (Inorder, Preorder and Postorder)
Unlike linear data structures (Array, Linked List, Queues, Stacks, etc) which have only one logical way to traverse them, trees can be traversed in different ways. Following are the generally used ways for traversing trees.

Example Tree
Example Tree

Depth First Traversals:
(a) Inorder (Left, Root, Right) : 4 2 5 1 3
(b) Preorder (Root, Left, Right) : 1 2 4 5 3
(c) Postorder (Left, Right, Root) : 4 5 2 3 1

Breadth First or Level Order Traversal : 1 2 3 4 5

```PYTHON
# Python program to for tree traversals 
  
# A class that represents an individual node in a 
# Binary Tree 
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  
  
# A function to do inorder tree traversal 
def printInorder(root): 
  
    if root: 
  
        # First recur on left child 
        printInorder(root.left) 
  
        # then print the data of node 
        print(root.val), 
  
        # now recur on right child 
        printInorder(root.right) 
  
  
  
# A function to do postorder tree traversal 
def printPostorder(root): 
  
    if root: 
  
        # First recur on left child 
        printPostorder(root.left) 
  
        # the recur on right child 
        printPostorder(root.right) 
  
        # now print the data of node 
        print(root.val), 
  
  
# A function to do preorder tree traversal 
def printPreorder(root): 
  
    if root: 
  
        # First print the data of node 
        print(root.val), 
  
        # Then recur on left child 
        printPreorder(root.left) 
  
        # Finally recur on right child 
        printPreorder(root.right) 
  
  
# Driver code 
root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5) 
print "Preorder traversal of binary tree is"
printPreorder(root) 
  
print "\nInorder traversal of binary tree is"
printInorder(root) 
  
print "\nPostorder traversal of binary tree is"
printPostorder(root) 
```
###### Inorder Tree Traversal without recursion and without stack!
https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
Using Morris Traversal, we can traverse the tree without using stack and recursion. The idea of Morris Traversal is based on Threaded Binary Tree. In this traversal, we first create links to Inorder successor and print the data using these links, and finally revert the changes to restore original tree.

1. Initialize current as root 
2. While current is not NULL
   If current does not have left child
      a) Print current’s data
      b) Go to the right, i.e., current = current->right
   Else
      a) Make current as right child of the rightmost 
         node in current's left subtree
      b) Go to this left child, i.e., current = current->left
```python
# Python program to do inorder traversal without recursion and  
# without stack Morris inOrder Traversal 
  
# A binary tree node 
class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
  
# Iterative function for inorder tree traversal 
def MorrisTraversal(root): 
      
    # Set current to root of binary tree 
    current = root  
      
    while(current is not None): 
          
        if current.left is None: 
            print current.data, 
            current = current.right 
        else: 
            # Find the inorder predecessor of current 
            pre = current.left 
            while(pre.right is not None and pre.right != current): 
                pre = pre.right 
   
            # Make current as right child of its inorder predecessor 
            if(pre.right is None): 
                pre.right = current 
                current = current.left 
                  
            # Revert the changes made in if part to restore the  
            # original tree i.e., fix the right child of predecssor 
            else: 
                pre.right = None
                print current.data, 
                current = current.right 
              
# Driver program to test above function 
"""  
Constructed binary tree is 
            1 
          /   \ 
        2      3 
      /  \ 
    4     5 
"""
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
  
MorrisTraversal(root) 
  
# This code is contributed by Naveen Aili 
```