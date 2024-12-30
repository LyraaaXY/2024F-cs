m, n = map(int, input().split())
tvs = sorted(list(map(int, input().split())))
count = 0
for i in range(n):
    if tvs[i] >= 0:
        break
    count -= tvs[i]
print(count)