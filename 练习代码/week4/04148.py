num = 1
while True:
    p, e, i, d = list(map(int,input().split()))
    if [p, e, i, d] == [-1, -1, -1 ,-1]:
        break
    P = [(p % 23) + _*23 for _ in range(924)]
    E = [(e % 28) + _*28 for _ in range(759)]
    I = [(i % 33) + _*33 for _ in range(644)]
    for j in range(644):
        if I[j] in E and I[j] in P:
            print('Case %d: the next triple peak occurs in %d days.'%(num, 21252 + I[j] - d) if d >= I[j] else 'Case %d: the next triple peak occurs in %d days.' %(num, I[j] - d))
            num += 1