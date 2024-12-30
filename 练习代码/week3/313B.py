string = list(i for i in input())
n = int(input())
res = []
for k in range(n):
    a,b = map(int,input().split())
    ans = 0
    for j in range(a,b):
        if string[j-1] == string[j]:
            ans += 1
    res.append(str(ans))
print('\n'.join(res))