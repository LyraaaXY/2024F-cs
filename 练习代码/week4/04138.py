import math
def is_prime(x):
    for i in range(2,math.floor(math.sqrt(x))+1):
        if x % i == 0:
            return False
    else:
        return True
n = int(input())
if n%2 != 0:
    print(2*(n -2))
else:
    for j in range(math.ceil(n//2),2,-1):
        if is_prime(j) == True and is_prime(n - j) == True:
            print(j * (n - j))
            break