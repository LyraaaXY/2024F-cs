from collections import deque

D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#dfs find a connected island
def dfs(x, y, n, maps, queue):
    maps[x][y] = '2'
    queue.append((x, y))
    for dx, dy in D:
        nx, ny = x + dx, y + dy
        if 0 <= nx <= n - 1 and 0 <= ny <= n - 1 and maps[nx][ny] == '1':
            dfs(nx, ny, n, maps, queue)

def bfs(queue, maps, n):
    steps = 0
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in D:
                nx, ny = x + dx, y + dy
                if 0 <= nx <= n - 1 and 0 <= ny <= n - 1:
                    if maps[nx][ny] == '1':
                        return steps
                    elif maps[nx][ny] == '0':
                        maps[nx][ny] = '2'
                        queue.append((nx, ny))
        steps += 1
    return steps

def main():
    n = int(input())
    maps = []
    for _ in range(n):
        maps.append(list(input()))
    queue = deque()

    for i in range(n):
        for j in range(n):
            if maps[i][j] == '1':
                dfs(i, j, n, maps, queue)
                return bfs(queue, maps, n)
            
if __name__ == "__main__":
    print(main())