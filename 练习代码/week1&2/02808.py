L,M = input().split()
tree = {number for number in range(int(L)+1)}
cut = set()
for i in range(int(M)):
    a,b = input().split()
    area = {j for j in range(int(a), int(b)+1)}
    cut = cut.union(area)
result = len(tree)-len(cut)
print(result)