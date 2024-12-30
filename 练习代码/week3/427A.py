n = int(input())
k = 0
skip = 0
occ = list(map(int,input().split()))
for i in range(n):
    k += occ[i]
    if k < 0:
        skip -= k
        k = 0
print(skip)