a,b,c = [], [], []

l1,r1 = map(int,input().split())
for i in range(l1):
    a.append(list(map(int,input().split())))
l2,r2 = map(int,input().split())
for i in range(l2):
    b.append(list(map(int,input().split())))
l3,r3 = map(int,input().split())
for i in range(l3):
    c.append(list(map(int,input().split())))

if r1 != l2 or l1 != l3 or r2 != r3:
    print('Error!')
else:
    for i in range(l3):
        for j in range(r3):
            c[i][j] += sum(a[i][k]*b[k][j] for k in range(r1))
    for i in range(l3):
        print(*c[i])