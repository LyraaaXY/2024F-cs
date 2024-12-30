import heapq

board = 1
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    print('Board #%d:' %(board))
    martix = [[' ']*(w + 2)]+[[' '] + list(input())+[' '] for _ in range(h)]  + [[' ']*(w + 2)]
    D = [(0,1), (0,-1), (1,0), (-1,0)]
    pair = 1
    while True:
        x1, y1, x2, y2 = map(int, input().split())
        if x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0:
            break
        queue, flag = [], False
        vis = set()
        heapq.heappush(queue, (0, x1, y1, -1))
        martix[y2][x2] = ' '
        vis.add((-1, x1, y1))
        while queue:
            step, x, y, dirs = heapq.heappop(queue)
            if x == x2 and y == y2:
                flag = True
                break
            for i, (dx,dy) in enumerate(D):
                a_x, a_y = x + dx, y + dy
                if 0 <= a_x <= w + 1 and 0 <= a_y <= h + 1 and (i, a_x, a_y) not in vis and martix[a_y][a_x] != "X":
                    vis.add((i, a_x, a_y))
                    heapq.heappush(queue, (step + (dirs != i), a_x, a_y, i))
        if flag:
            print(f"Pair {pair}: {step} segments.")
        else:
            print(f"Pair {pair}: impossible.")
        martix[y2][x2] = "X"
        pair += 1
    print()
    board += 1