m = int(input())
n = int(input())
nums = list(input().split())
nums.sort(key= lambda x:(x[0], len(x)), reverse = True)

dp = ['']*(m + 1)
vis = [[]]*(m + 1)
for i in range(m + 1):
    for j in range(n):
        if i == 0 or (dp[i] != '' and len(nums[j]) + i <= m and j not in vis[i]):
            if dp[i] + nums[j] > dp[i + len(nums[j])]:
                dp[i + len(nums[j])] = dp[i] + nums[j]
                vis[i + len(nums[j])] = vis[i] + [j]
for i in range(m, -1, -1):
    if dp[i] != '':
        print(dp[i])
        break