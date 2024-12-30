n = int(input())
numbers = list(map(int, input().split()))
num = [0]*(10**5 + 1)
dp = [0]*(10**5 + 1)
for i in range(n):
    num[numbers[i]] += numbers[i]
for i in range(1, 10**5 + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + num[i])
print(max(dp))