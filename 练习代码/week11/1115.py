def dfs(count, a, b):
    max_n, min_n = max(a, b), min(a, b)
    if max_n >= 2*min_n or max_n == min_n:
        return count
    else:
        return dfs(count + 1, max_n - min_n, min_n)

while True:
    a, b = map(int, input().split())
    if (a, b) == (0, 0):
        break
    print('win' if dfs(0, a, b)%2 == 0 else 'lose')