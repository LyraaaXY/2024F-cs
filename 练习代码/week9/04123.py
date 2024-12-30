D = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
ans = 0
def dfs(count, x, y):
    if count == m*n:
        global ans
        ans += 1
        return
    for ele in D:
        if maps[x + ele[0]][y + ele[1]] == 1:
            maps[x + ele[0]][y + ele[1]] = 0
            dfs(count + 1, x + ele[0], y + ele[1])
            maps[x + ele[0]][y + ele[1]] = 1

for t in range(int(input())):
    n, m , x, y = map(int, input().split())
    maps = [[0]*(m + 4)]*2 + [[0, 0] + [1 for _ in range(m)] + [0, 0] for i in range(n)] + [[0]*(m + 4)]*2
    ans = 0
    maps[x + 2][y + 2] = 0
    dfs(1, x + 2, y + 2)
    print(ans)