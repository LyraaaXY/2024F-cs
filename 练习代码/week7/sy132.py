def dfs(count, n, used, array, res):
    if count == n + 1:
        res.append(array[:]) 
        return
    for i in range(1, n + 1):
        if not used[i]:
            array.append(i)
            used[i] = True
            dfs(count + 1, n, used, array, res)
            used[i] = False
            array.pop()

def G(n):
    res = []
    used = [False]*(n + 1)
    dfs(1, n, used, [], res)
    
    for perm in res:
        print(' '.join(map(str, perm)))

n = int(input())
G(n)