from collections import Counter
n = int(input())
for i in range(n):
    s = int(input())
    n1 = int(input())
    sa = sorted(list(map(int,input().split())))
    n2 = int(input())
    sb = sorted(list(map(int,input().split())))
    res = 0
    for j in range(n1):
        if s - sa[j] in sb:
            res += Counter(sb)[s - sa[j]]
    print(res)