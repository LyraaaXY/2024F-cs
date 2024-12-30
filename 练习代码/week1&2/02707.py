import math

n = int(input())
for i in range(n):
    a, b, c = [float(number) for number in input().split()]
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b) / (2*a) + math.sqrt(delta) / (2*a)
        x2 = (-b) / (2*a) - math.sqrt(delta) / (2*a)
        print(f"x1={x1:.5f};x2={x2:.5f}")
    elif delta == 0:
        x = (-b) / (2*a)
        print(f"x1=x2={x:.5f}")
    else:
        x = (-b) / (2*a)
        sq = math.sqrt(-delta) / (2*a)
        print(f"x1={x:.5f}+{sq:.5f}i;x2={x:.5f}-{sq:.5f}i")