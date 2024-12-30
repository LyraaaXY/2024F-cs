n = int(input())
coins = sorted(list(map(int, input().split())))
coins.reverse()
value = sum(coins)
ive = 0
for i in range(n + 1):
    #ive += coins[i]
    if sum(coins[:i]) >= value//2 + 1:
        print(i)
        break