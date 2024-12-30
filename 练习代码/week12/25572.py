from collections import deque
D = [[1, 0], [-1, 0], [0, 1], [0, -1]]
def jud(maps, x, y):
    return 0 <= x < n and 0 <= y < n and maps[x][y] != '1'

def bfs(x, y, sta):
    queue, vis = deque([(x, y)]), set((x, y))
    while queue:
        x, y = queue.popleft()
        if maps[x][y] == '9' or maps[x + D[sta][0]][y + D[sta][1]] == '9':
            return 'yes'
        else:
            for i in range(4):
                nx, ny = x + D[i][0], y + D[i][1]
                if jud(maps, nx, ny) and jud(maps, nx + D[sta][0], ny + D[sta][1]) and (nx, ny) not in vis:
                    queue.append((nx, ny))
                    vis.add((nx, ny))
    return 'no'

n = int(input())
maps = []
for _ in range(n):
    maps.append(list(input().split()))
flag = True
for i in range(n):
    for j in range(n):
        if maps[i][j] == '5' and flag:
            if i + 1 < n and maps[i + 1][j] == '5':
                print(bfs(i, j, 0))
            else:
                print(bfs(i, j, 2))
            flag = False
            break