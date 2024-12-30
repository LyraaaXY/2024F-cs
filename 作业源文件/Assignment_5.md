# Assignment #5: Greedy穷举Implementation

Updated 1939 GMT+8 Oct 21, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 04148: 生理周期

brute force, http://cs101.openjudge.cn/practice/04148

思路：

根据已有数据，列举出一个完整大周期内所有的周期节点，然后寻找某单个共同值将它输出；需注意发生在所给日期前还是后进而作出处理

代码：

```python
num = 1
while True:
    p, e, i, d = list(map(int,input().split()))
    if [p, e, i, d] == [-1, -1, -1 ,-1]:
        break
    P = [(p % 23) + _*23 for _ in range(924)]
    E = [(e % 28) + _*28 for _ in range(759)]
    I = [(i % 33) + _*33 for _ in range(644)]
    for j in range(644):
        if I[j] in E and I[j] in P:
            print('Case %d: the next triple peak occurs in %d days.'%(num, 21252 + I[j] - d) if d >= I[j] else 'Case %d: the next triple peak occurs in %d days.' %(num, I[j] - d))
            num += 1
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241022233509691](C:\Users\lijh\AppData\Roaming\Typora\typora-user-images\image-20241022233509691.png)



### 18211: 军备竞赛

greedy, two pointers, http://cs101.openjudge.cn/practice/18211

思路：

在有钱的情况下购买最便宜的东西，如果钱已经不足以支撑继续购买，进行判断：卖掉最贵的武器能否让我回本？

进而完成循环

代码：

```python
p = int(input())
cost = sorted(list(map(int, input().split())))
w_m = 0
w_e = 0
total = len(cost)
while w_m + w_e < total:
    if cost[0] <= p:
        p -= cost[0]
        w_m += 1
        cost.remove(cost[0])
    else:
        if w_m > w_e and len(cost) > 1:
            p += max(cost)
            w_e += 1
            cost.pop()
        else:
            break
print(w_m - w_e)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241022233746950](C:\Users\lijh\AppData\Roaming\Typora\typora-user-images\image-20241022233746950.png)



### 21554: 排队做实验

greedy, http://cs101.openjudge.cn/practice/21554

思路：

现根据实验时间，再根据提交时间（人工添加赋值）对列表进行排序与计算

代码：

```python
n = int(input())
stu = list(map(int, input().split()))
stus = [[i + 1, stu[i]] for i in range(n)]
stus.sort(key = lambda x:(x[1], x[0]))
time = sum([(n - i - 1)*stus[i][1] for i in range(n)])/n
print(' '.join([str(stus[i][0]) for i in range(n)]))
print(f'{time:.2f}')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241025150157433](C:\Users\lijh\AppData\Roaming\Typora\typora-user-images\image-20241025150157433.png)



### 01008: Maya Calendar

implementation, http://cs101.openjudge.cn/practice/01008/

思路：

使用字典把不同的月份/天和数字对应起来，先通过累加还原具体天数，再进行整除（注意年数的处理）

因为一开始输出漏了输出(n) 卡了好久，以后要多注意

代码：

```python
habb = {'pop':1, 'no':2, 'zip':3, 'zotz':4, 'tzec':5, 'xul':6, 'yoxkin':7, 'mol':8, 'chen':9, 'yax':10, 'zac':11, 'ceh':12, 'mac':13, 'kankin':14, 'muan':15, 'pax':16, 'koyab':17, 'cumhu':18, 'uayet':19}
holly = {1:'imix', 2:'ik', 3:'akbal', 4:'kan', 5:'chicchan', 6:'cimi', 7:'manik', 8:'lamat', 9:'muluk', 10:'ok', 11:'chuen', 12:'eb', 13:'ben', 14:'ix', 15:'mem', 16:'cib', 17:'caban', 18:'eznab', 19:'canac', 0:'ahau'}

n = int(input())
print(n)
for i in range(n):
    d, m, y = input().split()
    day, month, year = int(d.replace('.', '')) + 1, habb[m], int(y)
    date = day + (month - 1)*20 + year*365
    Year = date//260
    if date%260 == 0:
        Year -= 1
    if date% 13 == 0:
        print('13 ' + holly[date%20] + ' ' + str(Year))
    else:
        print(str(date%13) + ' ' + holly[date%20] + ' ' + str(Year))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241023181456517](C:\Users\lijh\AppData\Roaming\Typora\typora-user-images\image-20241023181456517.png)

### 545C. Woodcutters

dp, greedy, 1500, https://codeforces.com/problemset/problem/545/C

思路：

每棵树只会影响其相邻的两棵树，左右两端的树直接暴力向两边倒不占据空间，进而进行计算

代码：

```python
n = int(input())
trees = []
for i in range(n):
    trees.append(list(map(int, input().split())))
count = 2
if n == 1:
    print(1)
else:
    for i in range(1, n - 1):
        if trees[i][0] - trees[i][1] > trees[i - 1][0]:
            count += 1
        elif trees[i][0] + trees[i][1] < trees[i + 1][0]:
            count += 1
            trees[i][0] += trees[i][1]
    print(count)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241025144947028](C:\Users\lijh\AppData\Roaming\Typora\typora-user-images\image-20241025144947028.png)

### 01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/

思路：

不断找某一个岛的雷达可投射范围的交集，不够了就重开一个新的，鉴于python集合形式较为单一，使用列表比较始末点

代码：

```python
import math

def f(d, islands):
    if d < 0:
        return -1
    count = 1
    ranges = []
    for [x, y] in islands:
        if y > d:
            return -1
        else:
            if y > d:
                return -1
        delta = math.sqrt(d * d - y * y)
        ranges.append((x - delta, x + delta))

    if not ranges:
        return -1

    ranges.sort(key=lambda x:x[1])
    r = ranges[0][1]
    for start, end in ranges[1:]:
        if r < start:
            r = end
            count += 1
    return count

case_num = 0
while True:
    n, d = map(int, input().split())
    if (n, d) == (0, 0):
        break
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))
    case_num += 1
    print('Case %d: %d' %(case_num, f(d, data)))
    input()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241025163251421](C:\Users\lijh\AppData\Roaming\Typora\typora-user-images\image-20241025163251421.png)

## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

最近精力没太放在做题上，有些跟不上，耗时又变长了，争取赶上进度。