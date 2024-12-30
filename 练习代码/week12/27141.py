n = int(input())
gift = list(map(int, input().split()))
data = [0]
for i in range(n):
    data.append(data[i] + gift[i] - 520)
money = {}
for i in range(n + 1):
    if data[i] in money.keys():
        money[data[i]][1] = i #更新最大索引，保证排序正常
    else:
        money[data[i]] = [i, i]
count = 0
for ele in money.values():
    count = max(ele[1] - ele[0], count)
print(count*520)