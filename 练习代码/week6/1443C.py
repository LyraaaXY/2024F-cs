t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    time = sorted([[A[_], B[_]] for _ in range(n)], reverse = True)
    res = 0
    for i in range(n):
        res += time[i][1]
        if time[i][0] <= res:
            res = max(time[i][0], res - time[i][1])
            break
    ans.append(res)
    print('\n'.join(map(str, ans)))