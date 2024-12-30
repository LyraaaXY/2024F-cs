import bisect

n, m = map(int, input().split())
coin = sorted(map(int, input().split()))
dp = [float('inf')] * (m + 1)
dp[0] = 0
for i in range(1, m + 1):
    w = bisect.bisect_right(coin, i)
    if w != 0:
        dp[i] = min(dp[i - coin[k]] for k in range(w)) + 1
print(dp[m] if dp[m] != float('inf') else -1)