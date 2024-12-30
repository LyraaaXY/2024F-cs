n, w = map(int, input().split())
price = list(map(int, input().split()))
weight = list(map(int, input().split()))
data = [[price[_], weight[_]] for _ in range(n)]

dp = [[0, 0]*n]
for i in range(n):
    for j in range(i - 1, -1, -1):
        if data[i][1] + dp[j][1] <= w:
            dp[i][0] = max(dp[i][0], dp[j][0] + data[i][0])
            dp[i][1] = dp[j][1] + data[i][1]
print(max(dp[i][0] for i in range(n)))