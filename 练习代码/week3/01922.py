import math

while True:
    n = int(input())
    if n == 0:
        break
    
    pre = float('inf')
    for i in range(n):
        a,b =map(int,input().split())
        if b < 0:
            continue
        res = math.ceil(4500*3.6/a + b)
        pre = min(pre,res)
    print(pre)