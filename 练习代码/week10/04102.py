n, m, k = map(int, input().split())
data = []
for i in range(k):
    data.append(list(map(int, input().split())))
dp = [[-1] * (m + 1) for _ in range(k + 1)]
dp[0][m] = n
for i in range(k):
    for p in range(m):
        for q in range(i + 1, 0, -1):
            if p + data[i][1] <= m and dp[q - 1][p + data[i][1]] != -1:
                dp[q][p] = max(dp[q][p], dp[q - 1][p + data[i][1]] - data[i][0])
def capture():
    for i in range(k, -1, -1):
        for j in range(m, -1, -1):
            if dp[i][j] != -1:
                return '%d %d' %(i, j)
print(capture())