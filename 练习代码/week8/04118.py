n, k = map(int, input())
from bisect import bisect_left

def max_profit(n, k, m, p):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        j = bisect_left(m, m[i-1] - k)
        dp[i] = max(dp[i-1], p[i-1] + dp[j])
    return dp[n]

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    m = list(map(int, input().split()))
    p = list(map(int, input().split()))
    print(max_profit(n, k, m, p))