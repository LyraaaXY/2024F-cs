n = int(input())
for i in range(n):
    k = int(input())
    prison  = [1 for _ in range(k)]
    for num in range(2,k+1):
        for j in range(k):
            if (j+1) % num == 0:
                prison[j] *= -1
    print((sum(prison)+k)//2)