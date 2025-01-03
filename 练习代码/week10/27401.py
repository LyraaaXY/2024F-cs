n, v = map(int, input().split())
a = list(map(int, input().split()))
sum_a = sum(a)
dp = [[-float("inf")] * (sum_a + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(sum_a + 1):
        if a[i - 1] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - a[i - 1]] + a[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]

if sum_a < v:
    print(0)
else:
    for k in range(v,sum_a+1):
        if dp[n][k] > 0:
            print(dp[n][k])
            break