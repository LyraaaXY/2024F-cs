D= [[-1, 0], [0, -1], [0, 1], [1, 0]]
def dfs(x, y):
    if dp[x][y] > 1:
        return dp[x][y]
    else:
        for ele in D:
                nx, ny = x + ele[0], y + ele[1]
                if 0 <= nx < m and 0 <= ny < n and h[nx][ny] < h[x][y]:
                    dp[x][y] = max(dfs(nx, ny) + 1, dp[x][y])
        return dp[x][y]

m, n = map(int, input().split())
h = []
for i in range(m):
    h.append(list(map(int, input().split())))
count = 0  
dp = [[1 for _ in range(n)] for _ in range(m)]
for i in range(m):
    for j in range(n):
        count = max(count, dfs(i, j))  
print(count)