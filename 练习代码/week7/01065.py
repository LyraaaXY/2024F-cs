t = int(input())
for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    sticks = [[data[2*i], data[2*i + 1]] for i in range(n)]
    
