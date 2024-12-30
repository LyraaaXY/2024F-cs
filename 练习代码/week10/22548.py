stock = list(map(int, input().split()))
n = len(stock)
dp = [0]*n
minstock = float('inf')
for i in range(1, n):
    minstock = min(minstock, stock[i])
    dp[i] = max(dp[i - 1], stock[i] - minstock)
print(dp[-1])