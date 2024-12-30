import heapq
m, n, p = map(int, input().split())
maps = [list(input().split())for _ in range(m)]
D = [[-1, 0], [1, 0], [0, 1], [0, -1]]
for _ in range(p):
    bx, by, ex, ey = map(int, input().split())
    if maps[bx][by] == '#' or maps[ex][ey] == '#':
        print('NO')
        continue
    queue, visit, res = [], set(), []
    heapq.heappush(queue, (0, bx, by))
    visit.add((bx, by, -1))
    while queue:
        steps, x, y = heapq.heappop(queue)
        if (x, y) == (ex, ey):
            res.append(steps)
        for i in range(4):
            nx, ny = x + D[i][0], y + D[i][1]
            if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] != '#' and (nx, ny, i) not in visit:
                energy = steps + abs(int(maps[nx][ny]) - int(maps[x][y]))
                heapq.heappush(queue, (energy, nx, ny))
                visit.add((nx, ny, i))
    print(min(res) if res else 'NO')