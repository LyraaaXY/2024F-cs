import math

def f(d, islands):
    if d < 0:
        return -1
    count = 1
    ranges = []
    for [x, y] in islands:
        if y > d:
            return -1
        else:
            if y > d:
                return -1
        delta = math.sqrt(d * d - y * y)
        ranges.append((x - delta, x + delta))

    if not ranges:
        return -1

    ranges.sort(key=lambda x:x[1])
    r = ranges[0][1]
    for start, end in ranges[1:]:
        if r < start:
            r = end
            count += 1
    return count

case_num = 0
while True:
    n, d = map(int, input().split())
    if (n, d) == (0, 0):
        break
    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))
    case_num += 1
    print('Case %d: %d' %(case_num, f(d, data)))
    input()