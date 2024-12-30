n = int(input())
while n > 1:
    if n % 2 == 0:
        n = n//2
        print('%d/2=%d' %(2 * n, n))
    else:
        n = 3 * n + 1
        print('%d*3+1=%d' %((n - 1)//3, n))
print('End')