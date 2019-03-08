# LeetCodeNote
## **347 ** 用QuickSelect重新做了一遍。关键是python的浅复制修改的还是原变量，所以list如果传入某个函数，然后在函数里修改了以后并不需要return了直接就在原地改了！
## Given an array of integers, find the median of the array.  What is the time complexity?  Can you do this in O(N) complexity?
QuickSelect

## How would you compute the running median of a stream of integers? 
一个小顶堆一个大顶堆
