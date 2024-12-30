import math

def is_prime(n):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
if n < 6 or n % 2 != 0:
    print('Error!')
else:
    for j in range(2, n//2 + 1):
        if is_prime(j) and is_prime(n-j):
            print('%d=%d+%d' % (n, j, n-j))