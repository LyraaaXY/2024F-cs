a,b = map(int,input().split())
ans = []
for i in range(a,b+1):
    num = [int(j)**3 for j in str(i)]
    if i == sum(num):
        ans.append(i)
if ans == []:
    print('NO')
else:
    print(' '.join(list(map(str,ans))))