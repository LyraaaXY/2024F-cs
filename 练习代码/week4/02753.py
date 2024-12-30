def fib(x):
    if x == 1 or x == 2:
        return 1
    else:
        fib = [1,1]
        for i in range(2,x):
            fib.append(fib[i-2]+fib[i-1])
        return fib[x-1]

n = int(input())
for j in range(n):
    print(fib(int(input())))