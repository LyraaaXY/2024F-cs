# Assignment #4: T-primes + 贪心



2024 fall, Complied by <mark>李婧涵，生科院



## 1. 题目

### 34B. Sale

greedy, sorting, 900, https://codeforces.com/problemset/problem/34/B



思路：先排序，判断是扛不动在先还是赚不了钱在先，结束



代码

```python
m, n = map(int, input().split())
tvs = sorted(list(map(int, input().split())))
count = 0
for i in range(n):
    if tvs[i] >= 0:
        break
    count -= tvs[i]
print(count)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241015152023781](C:\Users\lijh\AppData\Roaming\Typora\typora-user-images\image-20241015152023781.png)

### 160A. Twins

greedy, sortings, 900, https://codeforces.com/problemset/problem/160/A

思路：

倒序排序减少循环次数，求和比较，输出结果

代码

```python
n = int(input())
coins = sorted(list(map(int, input().split())))
coins.reverse()
value = sum(coins)
ive = 0
for i in range(n + 1):
    #ive += coins[i]
    if sum(coins[:i]) >= value//2 + 1:
        print(i)
        break

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241015154305864](C:\Users\lijh\AppData\Roaming\Typora\typora-user-images\image-20241015154305864.png)



### 1879B. Chips on the Board

constructive algorithms, greedy, 900, https://codeforces.com/problemset/problem/1879/B

思路：

这道题的最优解即：取每行最小的数相加/每列最小的数相加，再比较这两种取法哪个更小

代码

```python
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    min_c = min(a)*n + sum(b)
    min_l = min(b)*n + sum(a)
    print(min(min_c, min_l)) 

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241015154619067](C:\Users\lijh\AppData\Roaming\Typora\typora-user-images\image-20241015154619067.png)



### 158B. Taxi

*special problem, greedy, implementation, 1100, https://codeforces.com/problemset/problem/158/B

思路：

跟之前有道装包裹的题很想，这道题简化一点。

4，3个人的独立分装，2的两辆配对分装，剩下的1填进去

代码

```python
import math

n = int(input())
teams = input().split()
t_1, t_2, t_3, t_4 = teams.count('1'), teams.count('2'), teams.count('3'), teams.count('4')
res = t_4 + t_3 + math.ceil(t_2/2)
if t_1 > t_3 + 2*(math.ceil(t_2/2) - math.floor(t_2/2)):
    res += math.ceil((t_1 - (t_3 + 2*(math.ceil(t_2/2) - math.floor(t_2/2))))/4)
print(res)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241015154821125](C:\Users\lijh\AppData\Roaming\Typora\typora-user-images\image-20241015154821125.png)



### *230B. T-primes（选做）

binary search, implementation, math, number theory, 1300, http://codeforces.com/problemset/problem/230/B

思路：

感觉这道题老早了哈哈哈，

筛质数的方式最快的是欧拉筛，找到质数并删除以其为因数的合数，把j**2放入Tprime列表中

最大问题是一直超时（很奇怪，但是使用了欧拉筛还是超时），最后被迫放弃个人钻研学习了一下标答

代码

```python
import math

T_prime = []
number = [False]*2 + [True]*999999
for j in range(2,1000001):
    if number[j] == True:
        T_prime.append(j**2)
        for k in range(2, 1000000//j + 1):
            number[k*j] = False 
    
n = int(input())
rec = list(map(int, input().split()))
ans = []
for i in range(n):
    if rec[i] < 4 or int(rec[i]**0.5) != rec[i]**0.5:
        ans.append('NO')
    elif rec[i] in T_prime:
        ans.append('YES')
    else:
        ans.append('NO')
print('\n'.join(ans))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

（因为不是个人代码ac就不放了）



### *12559: 最大最小整数 （选做）

greedy, strings, sortings, http://cs101.openjudge.cn/practice/12559

思路：

不断的比较，交换

其实挺危险的，这个方法有一定超时的可能性，学习了一下另一种做法

代码

```python
n = int(input())
num = sorted(list(input().split()))
for i in range(n - 1):
    for j in range(i + 1, n):
        if num[j] + num[i] < num[i] + num[j]:
            num[i], num[j] = num[j], num[i]
mun = reversed(num)
print(''.join(mun) + ' ' + ''.join(num))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

进入算法学习后明显感受到迷茫，盯着题目但是脑子里一下子蹦不出来思路的情况经常出现

最近一段时间其他课业有点繁忙，每日一题落了四五题，争取快速赶上