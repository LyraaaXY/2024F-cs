d = int(input())
n = int(input())
screen = [[0]*1025 for _ in range(1025)]
for i in range(n):
    x, y, v = map(int, input().split())
    for j in range(max(x - d, 0), min(x + d, 1024) + 1):
        for k in range(max(y - d, 0), min(y + d, 1024) + 1):
            screen[j][k] += v
res_max = 0
count = 0
for l in range(1025):
    for m in range(1025):
        if screen[l][m] > res_max:
            res_max = screen[l][m]
            count = 1
        elif screen[l][m] == res_max:
            count += 1
print('%d %d' %(count, res_max))