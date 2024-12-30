while True:
    r, n = map(int,input().split())
    if (r, n) == (-1, -1):
        break
    army = sorted(list(map(int, input().split())))
    count = 0
    while len(army) >= 2:
        for i in range(1, len(army) - 1):
            if army[i] - army[0] > r:
                count += 1
                pre = army[i - 1] + r
                while army[0] <= pre:
                    army.remove(army[0])
    if len(army) == 1:
        count += 1
    print(count)