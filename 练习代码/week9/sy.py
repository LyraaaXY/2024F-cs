D = [[1, 0], [0, 1], [-1, 0], [0, -1]]
def dfs(x, y, count):
    global max_v, ans
    if (x, y) == (n - 1, m - 1):
        if count > max_v:
            max_v, ans = count, temp_path[:]
        
    visited[x][y] = True
    for ele in D:
        next_x, next_y = x + ele[0], y + ele[1]
        if 0 <= next_x < n and 0 <= next_y < m and not visited[next_x][next_y]:
            next_v = count + maps[next_x][next_y]
            temp_path.append((next_x, next_y))
            dfs(next_x, next_y, next_v)
            temp_path.pop()
    
    visited[x][y] = False

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

max_v = float('-inf')
ans = []
temp_path = [(0, 0)]
visited = [[False]*m for _ in range(n)]
dfs(0, 0, maps[0][0])
for x, y in ans:
    print(x + 1, y + 1)