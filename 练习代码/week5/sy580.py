n, m = map(int,input().split())
rec = []
res = 0
for i in range(n):
    rec.append(list(input().split()))
for j in range(n):
    for k in range(m):
        res = max(res, int(rec[j][k])*int(rec[0][k] + rec[j][m - 1] + rec[n - 1][k] + rec[j][0]))
print(res)