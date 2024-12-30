m, n = map(int, input().split())
spots = [[0]*(n + 2)]
C = 0
for i in range(m):
    spots.append([0] + list(map(int, input().split())) + [0])
spots.append([0]*(n + 2))
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if spots[i][j] == 1:
            C += 4 - spots[i][j - 1] - spots[i][j + 1] - spots[i - 1][j] - spots[i + 1][j]
print(C)