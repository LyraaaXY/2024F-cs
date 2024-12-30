m, n = map(int, input().split())
now = [[0]*(n + 2)]
refreshed = []
for i in range(m):
    now.append([0] + list(map(int, input().split())) + [0])
now.append([0]*(n + 2))
for j in range(1, m + 1):
    new = ['']*n
    for k in range(1, n + 1):
        status = sum(now[j - 1][k - 1: k + 2]) + now[j][k - 1] + now[j][k + 1] + sum(now[j + 1][k - 1: k + 2])
        if now[j][k] == 1:
            if status == 2 or status == 3:
                new[k - 1] = '1'
            else:
                new[k - 1] = '0'
        else:
            if status == 3:
                new[k - 1] = '1'
            else:
                new[k - 1] = '0'
    refreshed.append(new)
for _ in range(m):
    print(' '.join(refreshed[_]))