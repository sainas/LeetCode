# LeetCodeNote

## 215
https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/167837/Python-or-tm

Max Heap: Time: O(n + klog(n)) | Space: O(n)
Min Heap: Time: O(k) + O((n-k) * logk) | Space: O(K)
Quick select： O(n)

如果考虑k无限接近n
Max: O(n + nlog(n)) ~= O(nlogn)
Min: O(n + logk) ~= O(n)

如果考虑k = 0.5n
Max: O(n + nlogn)
Min: O(n + nlogn)

如果考虑n 无限大
Max: O(constant * n) 为什么是constant * n，参考
Min: O(log(k) * n)

所以几个例子比下来，还真说不清道不明哪个更好，大家千万以后不要机械化上来就写Min Heap，到时候面试官问起来Max和Min区别在哪，完全懵逼 (公瑾某家电面被问到这，然后没分析透，吃一堑长一智)
## 347

用QuickSelect重新做了一遍。关键是python的浅复制修改的还是原变量，所以list如果传入某个函数，然后在函数里修改了以后并不需要return了直接就在原地改了！
## Given an array of integers, find the median of the array.  What is the time complexity?  Can you do this in O(N) complexity?
QuickSelect

## How would you compute the running median of a stream of integers? 
一个小顶堆一个大顶堆
## 980
Python是没有办法pass by value的，所以如果在子函数中改了某个变量，再回到父函数想继续做时那个变量也已经变了，所以必须每一步都回到原值
```python
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
      
```
用C++可以有两种写法，我不会C++但是拿别人的试了一下也可以通过
g: passing by value
&g: passing by reference
*g: passing by pointer
```C++
// C++ passing by reference
// https://leetcode.com/problems/unique-paths-iii/discuss/221941/C%2B%2B-brute-force-DFS
class Solution {
public:
    int dfs(vector<vector<int>>& g, int i, int j, int s, int t_s) {
  if (i < 0 || j < 0 || i >= g.size() || j >= g[0].size() || g[i][j] == -1) return 0;
  if (g[i][j] == 2) return s == t_s ? 1 : 0;
  g[i][j] = -1;
  int paths = dfs(g, i + 1, j, s + 1, t_s) + dfs(g, i - 1, j, s + 1, t_s) +
    dfs(g, i, j + 1, s + 1, t_s) + dfs(g, i, j - 1, s + 1, t_s);
  g[i][j] = 0;
  return paths;
}
int uniquePathsIII(vector<vector<int>>& g) {
  auto i1 = 0, j1 = 0, t_steps = 0;
  for (auto i = 0; i < g.size(); ++i)
    for (auto j = 0; j < g[0].size(); ++j) {
      if (g[i][j] == 1) i1 = i, j1 = j;
      if (g[i][j] != -1) ++t_steps;
    }
  return dfs(g, i1, j1, 1, t_steps);
}
};
```
```c++
// C++ passing by value
// https://leetcode.com/problems/unique-paths-iii/discuss/221941/C%2B%2B-brute-force-DFS
class Solution {
public:
    int dfs(vector<vector<int>> g, int i, int j, int s, int t_s) {
  if (i < 0 || j < 0 || i >= g.size() || j >= g[0].size() || g[i][j] == -1) return 0;
  if (g[i][j] == 2) return s == t_s ? 1 : 0;
  g[i][j] = -1;
  int paths = dfs(g, i + 1, j, s + 1, t_s) + dfs(g, i - 1, j, s + 1, t_s) +
    dfs(g, i, j + 1, s + 1, t_s) + dfs(g, i, j - 1, s + 1, t_s);
  //g[i][j] = 0;
  return paths;
}
int uniquePathsIII(vector<vector<int>> g) {
  auto i1 = 0, j1 = 0, t_steps = 0;
  for (auto i = 0; i < g.size(); ++i)
    for (auto j = 0; j < g[0].size(); ++j) {
      if (g[i][j] == 1) i1 = i, j1 = j;
      if (g[i][j] != -1) ++t_steps;
    }
  return dfs(g, i1, j1, 1, t_steps);
}
};
```

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




相比于方法2，入队直接压入即可~
### Dijkstar's Algorithm
类似于带weight的bfs
但weight不能是复数
“无负权环的单源最短路径算法”
可以证明只要保存上一步的最短距离，就可以得到这一步的最短距离

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

### 背包问题，优先队列
[用优先队列式分支限界法解决0-1背包问题](https://blog.csdn.net/qq_24059821/article/details/51253704)
## Data Structure
### Complexity

![img](LeetCodeNote.assets/screen-shot-2018-04-28-at-174531.png)



### Tree

![postorder](LeetCodeNote.assets/145_transverse.png)

#### DFS
##### A summary of four traversal ways for each included recursive, iterative and morris traversal.
https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45740/Summary-of-preorder-inorder-postorder-four-traversal-ways-for-each

###### Recursive Way

**preorder**
```python
class Solution(object):
    def preorderTraversal(self, root):
        return ([root.val] + sum(map(self.preorderTraversal, (root.left, root.right)), [])) if root else []
```

**inorder**
```python
class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        
        left, right = map(self.inorderTraversal, (root.left, root.right))
        return left + [root.val] + right
```
**postorder**
```python
class Solution(object):
    def postorderTraversal(self, root):
        return (sum(map(self.postorderTraversal, (root.left, root.right)), []) + [root.val]) if root else []
```
###### Iterative Way With Stack + Visited State

**preorder**
```python
class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []

        stack, r = [[root, 0]], []
        while stack:
            top = stack[-1]

            if top[1]:
                stack.pop()
                if top[0].right:
                    stack.append([top[0].right, 0])
            else:
                r.append(top[0].val)
                top[1] = 1

                if top[0].left:
                    stack.append([top[0].left, 0])
        return r
```
**inorder**
```python
class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []

        stack, r, poped = [[root, 0]], [], False
        while stack:
            top = stack[-1]

            if top[1]:
                stack.pop()
                poped = True

                if top[0].right:
                    stack.append([top[0].right, 0])
                    poped = False

            elif top[0].left and not poped:
                stack.append([top[0].left, 0])
            else:
                r.append(top[0].val)
                top[1] = 1
        return r
```
**postorder**
```python
class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []

        stack, r = [[root, 0]], []
        while stack:
            top = stack[-1]

            if top[1]:
                stack.pop()
                if top[0].left:
                    stack.append([top[0].left, 0])
            else:
                r.append(top[0].val)
                top[1] = 1

                if top[0].right:
                    stack.append([top[0].right, 0])

        return r[::-1]
```
###### Iterative Way With Stack

This way was inspired by [Preorder, Inorder, and Postorder Iteratively Summarization](https://leetcode.com/discuss/71943/preorder-inorder-and-postorder-iteratively-summarization)

**preorder**
```python
class Solution(object):
    def preorderTraversal(self, root):
        stack, r = [], []
        while stack or root:
            if root:
                stack.append(root)
                r.append(root.val)
                root = root.left
            else:
                root = stack.pop().right
        return r
```
**inorder**
```python
class Solution(object):
    def inorderTraversal(self, root):
        stack, r = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                r.append(root.val)
                root = root.right
        return r
```
**postorder**
```python
class Solution(object):
    def postorderTraversal(self, root):
        stack, r = [], []
        while stack or root:
            if root:
                r.append(root.val)
                stack.append(root)
                root = root.right
            else:
                root = stack.pop().left

        return r[::-1]
```
###### Morris Traversal Way

**preorder**
```python
class Solution(object):
    def preorderTraversal(self, root):
        r = []
        while root:
            if not root.left:
                r.append(root.val)
                root = root.right
            else:
                pre = root.left
                while pre.right and pre.right != root:
                    pre = pre.right

                if not pre.right:
                    r.append(root.val)
                    pre.right = root
                    root = root.left
                else:
                    root = root.right
        return r
```
**inorder**
```python
class Solution(object):
    def inorderTraversal(self, root):
        r = []
        while root:
            if not root.left:
                r.append(root.val)
                root = root.right
            else:
                pre = root.left
                while pre.right and pre.right != root:
                    pre = pre.right

                if not pre.right:
                    pre.right = root
                    root = root.left
                else:
                    r.append(root.val)
                    root = root.right
        return r
```
**postorder**
```python
class Solution(object):
    def postorderTraversal(self, root):
        r = []
        while root:
            if not root.right:
                r.append(root.val)
                root = root.left
            else:
                next = root.right
                while next.left and next.left != root:
                    next = next.left

                if not next.left:
                    r.append(root.val)
                    next.left = root
                    root = root.right
                else:
                    root = root.left
        return r[::-1]
```
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

### Dynamic Programming
#### Tabulation vs Memoizatation
Tabulation: Bottom Up
Memoization: Top Down
|**Tabulation**|**Memoization**
state||easy to think
code ||easy (recursive)
speed|fast|slow(lot of recursive calls)
subproblem|if all subproblems must be solved more than onece, bottom-up is better|if not all subproblems need to be solved, top-down may be better
table entries|every entries is filled|not every

#### Two main type of a problem can use Dynamic programming:
1) Overlapping Subproblems
2) Optimal Substructure
### Heap
#### Time Complexity
**heapify O(n) **
假如有N个节点，那么高度为H=logN，最后一层每个父节点最多只需要下调1次，倒数第二层最多只需要下调2次，顶点最多需要下调H次，而最后一层父节点共有2^(H-1)个,倒数第二层公有2^(H-2),顶点只有1(2^0)个，所以总共的时间复杂度为s = 1 * 2^(H-1) + 2 * 2^(H-2) + ... + (H-1) * 2^1 + H * 2^0将H代入后s= 2N - 2 - log2(N)，近似的时间复杂度就是O(N)。

作者：wuxinliulei
链接：https://www.zhihu.com/question/20729324/answer/231955716
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
**binary heap insert O(logn)**
### Priorty Queue
和heap的区别：
优先队列可以用很多种方法实现，比如: linked list, binary heap, binomial heap, Fibonacci heap 等
他们对于不同的操作有不同的复杂度
比如最短路径的Dijkstra算法，该算法使用优先队列实现时，各个数据结构的时间复杂度是不同的，其中专门为该算法设计的斐波那契堆时间复杂度是最优的