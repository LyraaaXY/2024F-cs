n = int(input())

for i in range(n):
    a, b, c, d = [int(num) for num in input().split()]
    test = False
    for a_1 in [a, -a]:
        for b_1 in [b, -b]:
            for c_1 in [c, -c]:
                for d_1 in [d, -d]:
                    if a_1 + b_1 + c_1 + d_1 == 24:
                        test = True
    print('YES' if test else "NO")