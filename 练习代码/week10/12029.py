import sys
sys.setrecursionlimit(300000)
input = sys.stdin.read

def is_valid(x, y, m, n):
    return 0 <= x < m and 0 <= y < n

D = [[1, 0], [0, 1], [-1, 0], [0, -1]]
def dfs(x, y, m, n, water):
    for ele in D:
        a_x, a_y = ele[0] + x, ele[1] + y
        if is_valid(a_x, a_y, m, n) and water > maps[a_x][a_y]:
            if h[a_x][a_y] < water:
                h[x][y] = water
                dfs(a_x, a_y, m, n, water)

data = input().split()
count = 1
results = []

for _ in range(int(data[0])):
    m, n = map(int, data[count: count + 2])
    count += 2
    maps = []
    for i in range(m):
        maps.append(list(map(int, data[count: count + n])))
        count += n
    h = [[0]*n for _ in range(m)]

    i, j = map(int, data[count: count + 2])
    i, j = i - 1, j - 1
    count += 2

    p = data[count]
    count += 1
    for u in range(p):
        x, y = map(int, data[count: count + 2])
        x, y = x - 1, y - 1
        count += 2
        if maps[x][y] <= maps[i][j]:
            continue
        dfs(x, y, m, n, maps[x][y])

    results.append("Yes" if h[i][j] > 0  else "No")
print("\n".join(results))