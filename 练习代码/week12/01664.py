def apple(m, n):
    if m == 0:
        return 1
    if n == 1:
        return 1
    if m < n:
        return apple(m, m)
    else:
        return apple(m, m - 1) + apple(m - n, n)
    #dp[m][n−1] 表示至少有一个盘子空着的情况。, dp[m−n][n] 表示每个盘子至少放一个苹果的情况
