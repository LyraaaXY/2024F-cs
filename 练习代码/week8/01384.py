for t in range(int(input())):
    e, f = map(int, input().split())
    weight = f - e
    n = int(input())
    coins = []
    for i in range(n):
        coins.append(list(map(int, input().split())))
    dp = [0]*weight
    for num in range(weight + 1):
        for i in range(n):
            if (num == 0 or dp[num] != 0) and num + coins[i][1] <= weight:
                if dp[num + coins[i][1]] == 0:
                    dp[num + coins[i][1]] = coins[i][0]
                else:
                    dp[num + coins[i][1]] = min(dp[num] + coins[i][0], dp[num + coins[i][1]])
    print('This is impossible.' if dp[weight] == 0 else 'The minimum amount of money in the piggy-bank is %d.' %(dp[weight]))