while True:
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        hotels =list(tuple(map(int,input().split())))
    hotels.sort(key=lambda x:(x[0],x[1]))
            