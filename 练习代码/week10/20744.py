goods = list(map(int, input().split(',')))
n = len(goods)
dp = [[0,0] for _ in range(n)]
dp[0] = [goods[0]]*2
for i in range(1, n):
    dp[i][0] = max(dp[i - 1][0], 0) + goods[i]
    dp[i][1] = max(dp[i - 1][0], goods[i], dp[i - 1][1] + goods[i])
print(max(dp[i][1] for i in range(n)))