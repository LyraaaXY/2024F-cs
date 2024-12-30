connect = 0
D = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
def dfs(x, y):
    global connect
    if maps[x][y] == '.':
        return
    maps[x][y] = '.'
    connect += 1
    for ele in D:
        dfs(x + ele[0], y + ele[1])

for _ in range(int(input())):
    m, n = map(int, input().split())
    maps = [['.']*(n + 2)]
    for i in range(m):
        maps.append(['.'] + list(input()) + ['.'])
    maps.append(['.']*(n + 2))
    count = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if maps[i][j] == 'W':
                connect = 0
                dfs(i, j)
                count = max(count, connect)
    print(count)