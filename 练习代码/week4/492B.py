import math
n,l = map(int,input().split())
lamps = sorted(list(map(int,input().split())))
dis = [(lamps[i+1] - lamps[i])/2 for i in range(n-1)] + [lamps[0],l-lamps[n-1]]
light = max(dis)
print('%.9f'%light)