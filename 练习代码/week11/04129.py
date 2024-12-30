from collections import deque

D = [[1, 0],  [-1, 0], [0, 1], [0, -1]]
def bfs(x, y):
    queue, vis = deque([(0, x, y)]), set((0, x, y))
    while queue:
        step, dx, dy = queue.popleft()
        if maps[dx][dy] == 'E':
            return step
        else:
            for ele in D:
                nx, ny = dx + ele[0], dy + ele[1]
                if 0 <= nx < m and 0 <= ny < n and ((step + 1)%k, nx, ny) not in vis and (maps[nx][ny] != '#' or (step + 1)% k == 0):
                    queue.append((step + 1, nx, ny))
                    vis.add(((step + 1)%k, nx, ny))
    return 'Oop!'
for _ in range(int(input())):
    maps = []
    m, n, k = map(int, input().split())
    for i in range(m):
        maps.append(list(input()))
    for i in range(m):
        for j in range(n):
            if maps[i][j] == 'S':
                print(bfs(i, j))