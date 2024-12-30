n, m = map(int, input().split())
DP = [0] * 50
DP[0] = 1
for i in range(1, n + 1):
    if i < m:
        DP[i] = DP[i - 1] * 2 
    elif i == m:
        DP[i] = DP[i - 1] * 2 - 1
    else:
        DP[i] = DP[i - 1] * 2 - DP[i - m - 1]
print(DP[n])