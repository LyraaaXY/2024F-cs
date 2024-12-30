n = int(input().split())
array = list(map(int, input().split()))
dp = [0]*n
for i in range(1, n):
    if 