n = int(input())
pp = list(map(int,input().split()))
ins = []
out = []
mis = []
for i in range(len(pp)):
    if pp[i] > n:
        out.append(pp[i])
    else:
        ins.append(pp[i])
for j in range(1,n+1):
    if j not in ins:
        mis.append(j)
print(' '.join(list(map(str,mis))))
print(' '.join(list(map(str,sorted(out)))))