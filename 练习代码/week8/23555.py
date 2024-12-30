n, m1, m2 = map(int, input().split())
M1 = [[0 for _1 in range(n)] for _ in range(n)]
M2 = [[0 for _1 in range(n)] for _ in range(n)]
for i in range(m1):
    a, b, ele = map(int, input().split())
    M1[a][b] = ele
for i in range(m2):
    a, b, ele = map(int, input().split())
    M2[a][b] = ele
res = [[0 for _1 in range(n)] for _ in range(n)]
ans = []
for i in range(n):
    for j in range(n):
        for k in range(n):
            res[i][j] += M1[i][k]*M2[k][j]
        if res[i][j] != 0:
            ans.append([i, j, res[i][j]])
for num in ans:
    print(' '.join(map(str, num)))