# Python Note
## decimal to binary

```
bin(1)[2:].zfill(8)
```
will print '00000001'
## Function
### ord()
The ord() method is the inverse of chr().
Return Unicode
ASCII is a subset of Unicode
```
ord('a')
```
Output:97

### reduce()

### filter(function, sequence)



```
def f(x): return x != 'a' 
filter(f, "abcdef") 

'bcdef'
```
## collections
### Counter()
是Dict的一个子类
```
from collections import Counter
Counter(nums).most_common(k)
```
### deque()
有popleft() 和 pop()
还可以直接外加list()转换成list
deque(['f', 'g', 'h', 'i', 'j'])
初始化如果要加pair一定要`queue = collections.deque([(1,2)])`
result: `deque([(1, 2)])`
不能`queue = collections.deque((1,2))`否则不管加多少层括号都不对,都不会是pair而是两个独立的数
wrong result: `deque([1, 2])`

## itertools
### compress()
compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
