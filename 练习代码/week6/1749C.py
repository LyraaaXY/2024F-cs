t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    rec = sorted(list(map(int, input().split())))
    k = 1
    Flag = True
    while k <= n and Flag:
        num = rec
        for i in range(1, k + 1):
            flag = True
            for j in range(n - i, -1, -1):
                if num[j] <= k - i + 1 and flag:
                    num.remove(num[j])
                    flag = False
            if flag:
                res = k - 1
                Flag = False
                break
            else:
                num[0] += k - i + 1
                num.sort()
                print(num)
        k += 1
    ans.append(res)
print('\n'.join(map(str, ans)))