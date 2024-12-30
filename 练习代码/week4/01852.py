n = int(input())
for i in range(n):
    dis, num = map(int,input().split())
    pos = list(map(int,input().split()))
    time_max = max(dis - min(_ for _ in pos),max(_ for _ in pos))
    time_min = max(min(_,dis-_) for _ in pos)
    print('%d %d'%(time_min,time_max))
    