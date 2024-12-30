n = int(input())
dp = [1] + [0]*n
for i in range(n):
    for j in range(1, n + 1 - i):
        dp[i + j] += dp[i]
print(dp[n])