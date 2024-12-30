m, n, p, q = map(int,input().split())
rec = []
index = []
for i in range(m):
    rec.append(list(map(int, input().split())))
for j in range(p):
    index.append(list(map(int, input().split())))
def pro(u, v):
    pro = 0
    for k in range(p):
        for l in range(q):
            pro += rec[u + k][v + l]*index[k][l]
    return pro
for a in range(m + 1 - p):
    ans = []
    for b in range(n + 1 - q):
        ans.append(pro(a,b))
    print(' '.join(map(str, ans)))