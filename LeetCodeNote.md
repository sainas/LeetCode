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

## Complexity

![img](LeetCodeNote.assets/screen-shot-2018-04-28-at-174531.png)