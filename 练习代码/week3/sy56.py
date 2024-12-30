n = int(input())
q = 0
num = list(map(int,input().split()))
for j in range(n-1):
    if num[j] > num[j+1]:
        print('NO')
        break
    else:
        q += 1
if q == n-1:
    print('YES')