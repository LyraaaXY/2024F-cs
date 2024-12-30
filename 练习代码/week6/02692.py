full = set('ABCDEFGH')
n = int(input())
for i in range(n):
    mem ={'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'J': 0, 'K': 0, 'L': 0}
    for j in range(3):
        x, y, judge = input().split()
        coins = set(x)|set(y)
        if judge == 'even':
            for ele in coins:
                mem[ele] = 0
        else:
            for ele in full - coins:
                mem[ele] = 0
            if judge == 'up':
                for ele_1 in