# LeetCodeNote
## **347 ** 

用QuickSelect重新做了一遍。关键是python的浅复制修改的还是原变量，所以list如果传入某个函数，然后在函数里修改了以后并不需要return了直接就在原地改了！
## Given an array of integers, find the median of the array.  What is the time complexity?  Can you do this in O(N) complexity?
QuickSelect

## How would you compute the running median of a stream of integers? 
一个小顶堆一个大顶堆

## 学习map reduce filter lambda
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