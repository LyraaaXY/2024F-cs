n, b = map(int, input().split())
*p, = map(int, input().split())
*w, = map(int, input().split())

dp=[0]*(b+1)
for i in range(n):
    for j in range(b, w[i] - 1, -1):
        dp[j] = max(dp[j], dp[j-w[i]]+p[i])
            
print(dp[-1])