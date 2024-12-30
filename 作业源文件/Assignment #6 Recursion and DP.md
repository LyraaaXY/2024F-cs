# Assignment #6: Recursion and DP

Updated 2201 GMT+8 Oct 29, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### sy119: 汉诺塔

recursion, https://sunnywhy.com/sfbj/4/3/119  

思路：

经过纸上运算，发现要移动n层，就必须先把前n - 1层移动到中间的柱子才能移动最大的圆盘，因此逻辑为

把前n-1层从f移动到m ——》把大圆盘从f移动到b——》把前n-1层从m移动到

代码：

```python
n = int(input())
def F(n, f, m, b):
    if n == 0:
        return []
    else:
        return F(n - 1, f, b, m) + [f + '->' + b] + F(n - 1, m, f, b)
print(2**n - 1)
print('\n'.join(F(n, 'A', 'B', 'C')))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241031114141229](C:\Users\lijh\AppData\Roaming\Typora\typora-user-images\image-20241031114141229.png)

### sy132: 全排列I

recursion, https://sunnywhy.com/sfbj/4/3/132

思路：

学习了dfs， 先排列未使用的数字再进行回溯

代码：

```python
def dfs(count, n, used, array, res):
    if count == n + 1:
        res.append(array[:]) 
        return
    for i in range(1, n + 1):
        if not used[i]:
            array.append(i)
            used[i] = True
            dfs(count + 1, n, used, array, res)
            used[i] = False
            array.pop()

def G(n):
    res = []
    used = [False]*(n + 1)
    dfs(1, n, used, [], res)
    
    for perm in res:
        print(' '.join(map(str, perm)))

n = int(input())
G(n)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241102111748662](C:\Users\lijh\AppData\Roaming\Typora\typora-user-images\image-20241102111748662.png)



### 02945: 拦截导弹 

dp, http://cs101.openjudge.cn/2024fallroutine/02945

思路：

从最后一个数开始寻找，寻找以这个数为开头的列表可容纳数的zui'da

代码：

```python
k = int(input())
bombs = list(map(int, input().split()))
dp = [0]*k
for i in range(k-1, -1, -1):
    count = 1
    for j in range(k -1, i, -1):
        if bombs[i] >= bombs[j] and dp[j] + 1 > count:
            count += 1
    dp[i] = count
print(max(dp))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 23421: 小偷背包 

dp, http://cs101.openjudge.cn/practice/23421

思路：

没想出思路，直接看的答案找初步思路，后续又发现自己从0开始遍历的代码有缺陷，进行修改

代码：

```python
n, b = map(int, input().split())
*p, = map(int, input().split())
*w, = map(int, input().split())

dp=[0]*(b+1)
for i in range(n):
    for j in range(b, w[i] - 1, -1):
        dp[j] = max(dp[j], dp[j-w[i]]+p[i])
            
print(dp[-1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241101001004681](C:\Users\lijh\AppData\Roaming\Typora\typora-user-images\image-20241101001004681.png)



### 02754: 八皇后

dfs and similar, http://cs101.openjudge.cn/practice/02754

思路：

看的答案，优先输出大的字母，后续对没使用的数字进行排列，如果不够了再找小一点的数字

代码：

```python
answer = []

def Queen(s):
    for col in range(1, 9):
        for j in range(len(s)):
            if (str(col) == s[j] or abs(col - int(s[j])) == abs(len(s) - j)): # 两个皇后不能在同一斜线
                break
        else:
            if len(s) == 7:
                answer.append(s + str(col))
            else:
                Queen(s + str(col))

Queen('')

n = int(input())
for _ in range(n):
    a = int(input())
    print(answer[a - 1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241102203422397](C:\Users\lijh\AppData\Roaming\Typora\typora-user-images\image-20241102203422397.png)



### 189A. Cut Ribbon 

brute force, dp 1300 https://codeforces.com/problemset/problem/189/A

思路：

借鉴了背包的思维，一个坑点是会超范围，逻辑要理清。

代码：

```python
n, a, b, c = map(int, input().split())
dp = [0]*(n + 1)
for i in range(0, n + 1):
    for num in set([a, b, c]):
        if (i == 0 or dp[i] !=0) and i + num <= n:
            dp[i + num] = max(dp[i + num], dp[i] + 1)
print(dp[n])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241031234124725](C:\Users\lijh\AppData\Roaming\Typora\typora-user-images\image-20241031234124725.png)

## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

每日选做争取跟着进度做。

dp挺难的，这次作业除了汉诺塔和割绳子都是想不出来了去看了答案才会的，但是跟着作业思路走逐渐理解的过程很有意思。