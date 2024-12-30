n = int(input())
for i in range(n):
    ang = int(input())
    if 360%(180-ang) == 0:
        print('YES')
    else:
        print('NO')