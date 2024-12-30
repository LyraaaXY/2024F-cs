n = int(input())
pre = list(input())
for i in range(n-1):
    ans = []
    res = list(input())
    for j in range(0,min(len(pre),len(res))):
        if pre[j] == res[j]:
            ans.append(pre[j])
        else:
            pre.clear()
            pre = ans
            break
print(''.join(pre))