n, a, b, c = map(int, input().split())
dp = [0]*(n + 1)
for i in range(0, n + 1):
    for num in set([a, b, c]):
        if (i == 0 or dp[i] !=0) and i + num <= n:
            dp[i + num] = max(dp[i + num], dp[i] + 1)
print(dp[n])