ma = []
i = 1
while i < 6:
    line = list(map(int,input().split()))
    if sum(line) == 1:
        r = i
    ma.append(line)
    i += 1
for j in range(5):
    if ma[0][j] + ma[1][j] + ma[2][j] + ma[3][j] +ma[4][j] == 1:
        c = j + 1
        break
print(abs(3-r) + abs(3-c))