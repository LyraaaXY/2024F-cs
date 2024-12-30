n, m = map(int, input().split())
points = list(map(int, input().split()))
res = sum([points[num]*(-1)**num for num in range(n)]) + (m + m*(-1)**n)//2
for i in range(1, m):
    if i not in points:
        points_1 = sorted([i] + points)
        res = max(res, sum([points_1[num]*(-1)**num for num in range(n + 1)]) + (m + m*(-1)**(n + 1))//2)
print(res)