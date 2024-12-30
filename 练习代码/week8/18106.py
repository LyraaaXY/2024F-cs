def generate_blocks(n):
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1, 2], [4, 3]]
    block = [[0] * n for _ in range(n)]
    
    block[0] = list(range(1, n + 1))
    block[n - 1] = list(range(3 * n - 2, 2 * n - 2, -1))
    for i in range(1, n - 1):
        block[i][0] = 4 * n - 3 - i
        block[i][n - 1] = n + i
    if n > 2:
        inner_block = generate_blocks(n - 2)
        offset = 4 * (n - 1)
        for i in range(n - 2):
            for j in range(n - 2):
                block[i + 1][j + 1] = inner_block[i][j] + offset
    return block

n = int(input())
block = generate_blocks(n)

for row in block:
    print(' '.join(map(str, row)))