t = int(input())
pre = 10**5
ans = 0
num = sorted(list(map(int, input().split())))
i, j = 0, len(num) - 1
while i < j:
    add = num[i] + num[j] - t
    if add == 0:
        ans = t
        break
    else:
        if abs(add) == abs(pre):
            ans = min(add + t, pre + t)
        if abs(add) < abs(pre):
            ans = t + add
            pre = add
        if add > 0:
            j -= 1
        else:
            i += 1

print(ans)