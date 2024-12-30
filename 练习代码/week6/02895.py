k = int(input())
bombs = list(map(int, input().split()))
dp = [0]*k
for i in range(k-1, -1, -1):
    count = 1
    for j in range(k -1, i, -1):
        if bombs[i] >= bombs[j] and dp[j] + 1 > count:
            count += 1
    dp[i] = count
print(max(dp))