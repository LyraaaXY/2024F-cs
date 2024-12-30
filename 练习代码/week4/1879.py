t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    min_c = min(a)*n + sum(b)
    min_l = min(b)*n + sum(a)
    print(min(min_c, min_l)) 