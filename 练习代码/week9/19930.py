q = []
D = [[0, 1], [1, 0], [-1, 0], [0, -1]]
vis = [[0] * 52 for _ in range(52)]
maps = []

m, n = map(int, input().split())
for i in range(m):
    maps.append(list(map(int, input().split())))

def check(x, y):
    if (x < 0 or y < 0 or x >= m or y >= n):
        return False
    if (vis[x][y] or maps[x][y] == 2):
        return False
    return True

q.append((0, 0))
begin, end = 0, 1
level = 0
while begin < end:
    for k in range(begin, end):
        x, y = q[begin]
        begin += 1
        if (maps[x][y] == 1):
            print(level)
            exit(0)     
        for ele in D:
            next_x, next_y = x + ele[0], y + ele[1]
            if (check(next_x, next_y)):
                vis[next_x][next_y] = 1
                q.append((next_x, next_y))
                end += 1
    level += 1
print('NO')