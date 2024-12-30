n, q = map(int,input().split())
rel = []
for i in range(q):
    p = list(map(int,input().split()))
    rel.append(p)
flag = False
for j in range(q):
    for k in range(q):
        for l in range(q):
            if rel[j][1] == rel[k][0] and rel[k][1] == rel[l][0] and rel[l][1] == rel[j][0]:
                flag = True
                break
print('Yes' if flag == True else 'No')