num = []
k = 2
while k < 10**14:
    num.append(k)
    k *= 2

n = int(input())
for i in range(n):
    a = int(input())
    print('NO' if a in num else 'YES')