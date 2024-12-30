from collections import deque
D = [[1, 0], [-1, 0], [0, 1], [0, -1]]
def good(maps):
    count = 0
    for i in range(m):
        for j in range(n):
            if maps[i][j] == 1:
                count += 1
    return count

def bfs(x, y, fresh, maps):
    queue, vis = deque([(0, fresh, x, y)]), set((x, y))
    while queue:
        step, fresh_1, bx, by = queue.popleft()
        if fresh_1 == 0:
            return step
        else:
            for ele in D:
                nx, ny = bx + ele[0], by + ele[1]
                if 0 <= nx < m and 0 <= ny < n and (x, y) not in vis and maps[nx][ny] == 1:
                    queue.append((step + 1, fresh_1 -1, nx, ny))
                    vis.add((nx, ny))
    return -1

fresh = good(grid)
res = float('inf')
for i in range(m):
    for j in range(n):
        if grid[i][j] == 2:
            res = min(res, bfs(i, j, fresh, grid))
return res