n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
div = (n - 1)//2
res = []
if n%2 != 0:
    res.append(data[div][div])
else:
    res.append(sum(data[div][div:div + 2]) + sum(data[div + 1][div:div + 2]))

for i in range(div - 1, -1, -1):
    add = 0
    for j in range(i, n - i):
        add += sum(data[j][i: n - i])
    res.append(add - sum(res))

print(max(res))