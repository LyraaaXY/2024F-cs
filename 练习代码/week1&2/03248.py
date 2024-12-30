import math
while True:
    try:
        a,b = [int(number) for number in input().split()]
        print(math.gcd(a,b))
    except EOFError:
        break