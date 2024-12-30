n = int(input())
m = 0
for a in range(n,-1,-1):
    for b in range(n,-1,-1):
        for c in range(n,-1,-1):
            if (a + b)%2 == 0 and (b + c)%3 == 0 and (a + b + c)%5 == 0:
                m = max(m, a + b + c)
                break