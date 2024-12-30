m = 10**9+7
n, k, d = map(int, input().split())
normal = [1] + [0]*n
produce = [1] + [0]*n
for i in range(1, n + 1):
    normal[i] = sum(normal[max(i - k, 0): i])%m
    produce[i] = sum(produce[max(i - d + 1, 0): i])%m
print((normal[i] - produce[i] + m)%m)