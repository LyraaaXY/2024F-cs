t = int(input())
for i in range(t):
    coins = [0, 0]
    num = int(input())
    n = 0
    while num > 0:
        if num%2 == 1:
            num -= 1
            coins[n%2] += 1
        else:
            if num%4 == 0 and num != 4:
                num -= 1
                coins[n%2] += 1
            else:
                num = num//2
                coins[n%2] += num
        n += 1
    print(coins[0])