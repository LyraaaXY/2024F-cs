t, k = map(int, input().split())
dp = [1]*k + [0]*(10**5 + 1 - k)
S = [i for i in range(k)] + [0]*(10**5 + 1 - k)
for i in range(k, 10**5 + 1):
    dp[i] = (dp[i - 1] + dp[i - k])%(10**9 + 7)
    S[i] = (S[i - 1] + dp[i])%(10**9 + 7)
for _ in range(t):
    begin, end = map(int, input().split())
    print((S[end] - S[begin - 1] + 10**9 + 7)%(10**9 + 7))