from bisect import bisect_left

n = int(input())
height = list(map(int, input().split()))
height.reverse()
dp = []
for i in range(n):
    j = bisect_left(dp, height[i])
    if j >= len(dp):
        dp.append(height[j])
    else:
        dp[j] = height[i]
print(len(dp))