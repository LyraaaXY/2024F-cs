# assignment 2

## 263A beautiful matrix

**思路**：输入完成后找到相加和为1的行/列即可

（为了简化，在输入过程中就先找到行）

**代码：**

```python
ma = []

i = 1

while i < 6:

  line = list(map(int,input().split()))

  if sum(line) == 1:

​    r = i

  ma.append(line)

  i += 1

for j in range(5):

  if ma[0][j] + ma[1][j] + ma[2][j] + ma[3][j] +ma[4][j] == 1:

​    c = j + 1

​    break

print(abs(3-r) + abs(3-c))
```

![image-20240924153156489](C:\Users\lijh\AppData\Roaming\Typora\typora-user-images\image-20240924153156489.png)

## 1328A Divisibility Problem

**思路：**先判断是否整除，整除直接输出，不整除就找到最近整除项相减

**代码：**

```python
n = int(input())

for i in range(n):

  a,b = map(int,input().split())

  if a%b == 0:

​    print(0)

  else:

​    print((a//b+1)*b -a)


```

![image-20240924155858505](C:\Users\lijh\AppData\Roaming\Typora\typora-user-images\image-20240924155858505.png)

## 427A Police Recruits

**思路：**既然之后招聘的警官无法解决先前的案件，那就只要检测到无法解决的案件就记录（即只要和为负数就记录），之后清零防止后续招聘的警官影响

**代码：**

```python
n = int(input())

k = 0

skip = 0

occ = list(map(int,input().split()))

for i in range(n):

  k += occ[i]

  if k < 0:

​    skip -= k

​    k = 0

print(skip)
```

![image-20240924164135651](C:\Users\lijh\AppData\Roaming\Typora\typora-user-images\image-20240924164135651.png)

## 02808 校门外的树

**思路：**（一开始错误版） 总-每次扣除数，没有考虑到重合

发现错误后改用集合，并集计算后总元素数-扣除元素数

**代码：**

```python
L,M = input().split()

tree = {number for number in range(int(L)+1)}

cut = set()

for i in range(int(M)):

  a,b = input().split()

  area = {j for j in range(int(a), int(b)+1)}

  cut = cut.union(area)

result = len(tree)-len(cut)

print(result)
```

![img](file:///C:/Users/lijh/AppData/Local/Temp/msohtmlclip1/01/clip_image014.png)

## sy60 水仙花数

**思路：**获得输入范围➡分割获得每一位的数➡计算

**代码：**

```python
a,b = map(int,input().split())

ans = []

for i in range(a,b+1):

  num = [int(j)**3 for j in str(i)]

  if i == sum(num):

​    ans.append(i)

if ans == []:

  print('NO')

else:

  print(' '.join(list(map(str,ans))))
```



## 01922 Ride to school

**思路：**
(初始) 每一秒返回不同人的骑行状态，后来发现个人语法实力不够难以实现且过于繁琐

（个人思路优化后）找到还未出发的人，找到那个人的最短出行时间即可

**代码：**

```python
import math

while True:

  n = int(input())

  if n == 0:

​    break

  

  pre = float('inf')

  for i in range(n):

​    a,b =map(int,input().split())

​    if b < 0:

​      continue

​    res = math.ceil(4500*3.6/a + b)

​    pre = min(pre,res)

  print(pre)


```

![image-20240924174531629](C:\Users\lijh\AppData\Roaming\Typora\typora-user-images\image-20240924174531629.png)

## 个人总结收获
进步期，做题速度飞升，但是随着习题难度的提升，明显感受到逻辑有时候的卡顿，目前每日两题都按时完成，争取继续加快做题速度，用题量堆积换来逻辑思维打通。