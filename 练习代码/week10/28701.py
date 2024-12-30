n, k = map(int, input().split())
chicks = list(map(int, input().split()))
chicks.sort()
s = sum(chicks)
for i in range(n - 1, -1, -1):
    if chicks[i] > s / k:
        s -= chicks[i]
        k -= 1
print('%.3f' %(s / k))