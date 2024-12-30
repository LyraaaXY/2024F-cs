n = int(input())
num = list(map(int, input().split()))
dp = [0]*n
for i in range(n - 1, -1, -1):
    count = 1
    for j in range(n - 1, i, -1):
        if num[i] < num[j]:
            dp[i] = max(dp[j] + 1, dp[i])
print(max(dp))