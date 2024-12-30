n = int(input())
old = []
young = []
count = 0
for i in range(n):
    a, b = input().split()
    if int(b) < 60:
        young.append(a)
    else:
        old.append([a, int(b), count])
        count -= 1
old.sort(key = lambda x:(x[1], x[2]), reverse = True)
old_res = [num[0] for num in old]
print('\n'.join(old_res))
print('\n'.join(young))