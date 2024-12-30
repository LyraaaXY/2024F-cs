n, m = map(int, input().split())
nums = list(map(int, input().split()))
dp = [1]*n
data = []
for i in range(n - 1, -1, -1):
    if nums[i] not in data:
        data.append(nums[i])
    dp[i] = len(data)
for j in range(m):
    num = int(input())
    print(dp[num - 1])