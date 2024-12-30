n, q = map(int,input().split())
rel = []
for i in range(q):
    x, y = map(int, input().split())
    rel.append([x, y])
flag = False
for j in range(q):
    for k in range(q):
        if rel[j][0] == rel[k][1] and rel[j][1] == rel[k][0]:
            flag = True
            break
print('Yes' if flag == True else 'No')