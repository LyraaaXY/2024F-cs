import math
while True:
    pack = list(map(int,input().split()))
    rest = [0,5,3,1]
    if sum(pack) == 0:
        break
    box = sum(pack[3:6])
    box += math.ceil(pack[2]/4)
    if pack[1] > 5*pack[3] + rest[pack[2]%4]:
        box += math.ceil((pack[1] - 5*pack[3] - rest[pack[2]%4])/9)
    space = box * 36 - sum([((i+1)**2) * pack[i] for i in range(1,6)])
    if pack[0] > space:
        box += math.ceil((pack[0] - space)/36)
    print(box)