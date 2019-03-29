# Python Note
## copy and deepcopy
```python
import copy
a = [1, 2, [3, 4], 5]
b1 = a
b2 = copy.copy(a)
b3 = copy.deepcopy(a)
a[0]='test'
a[3].append('999')
```
b1: ['test', 2, [3, 4, 999], 5]
b2: [1, 2, [3, 4, 999], 5]
b3: [1, 2, [3, 4], 5]

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



```python
def f(x): return x != 'a' 
filter(f, "abcdef") 

'bcdef'
```
```python
a = [None,1,3,None,2,None,4]
filter(None,a)

[1,3,2,4]
```
```python
a = [None,1,0,None,2,None,4]
filter(None,a)

[1,2,4]
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

### product()


Cartesian product of input iterables.
```
product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
```

product('ABCD', repeat=2)	 |	AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
permutations('ABCD', 2)	 	|AB AC AD BA BC BD CA CB CD DA DB DC
combinations('ABCD', 2)	 |	AB AC AD BC BD CD
combinations_with_replacement('ABCD', 2)	 |	AA AB AC AD BB BC BD CC CD DD

### combinations()
### permutations()
