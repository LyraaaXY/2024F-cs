n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
data.sort(key = lambda x:x[1])
dp = [0]*61
date = [True]*61
count = 0
for i in range(61):
    if i > 0:
        dp[i] = dp[i - 1]
    for j in range(count, n):
        if data[j][1] > i:
            count = j
            break
        else:
            if False not in date[data[j][0]: data[j][1] + 1]:
                dp[i] += 1
                for num in range(data[j][0], data[j][1] + 1):
                    date[num] = False
print(dp[60])