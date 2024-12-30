import math

n = int(input())
for a in range(3,n+1):
    for b in range(2,math.floor(a/math.cbrt(3))):
        for c in range(b,math.floor(math.cbrt((a**3-b**3)/2))+1):
            for d in range(c,math.floor(math.cbrt(a**3-b**3-c**3)+1)):
                if a**3 == b**3 +c**3 +d**3:
                    print('Cube = %d, Triple = (%d,%d,%d)'%(a,b,c,d))