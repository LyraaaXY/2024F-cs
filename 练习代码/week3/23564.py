import math

n = int(input())
div = []
q = 0
for i in range(2, n+1):
    if n % i == 0:
        div.append(i)
        if n % i**2 == 0:
            q += 1
        n = n//i
if len(div) % 2 == 0  and q == 0:
    print(1)
elif len(div) % 2 != 0 and q == 0:
    print(-1)
else:
    print(0)