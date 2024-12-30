n = int(input())
if n == 1:
    print(n)
else:
    dp = [1]*2 + [0]*(n - 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[n])