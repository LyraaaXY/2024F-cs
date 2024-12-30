import sys
input = sys.stdin.read
data = input().split()

t, m = map(int, data[:2])
medicine = []
dp = [0]*(t + 1)
for k in range(m):
    medicine.append(data[2*k + 2: 2*k + 4])

for ele in medicine:
    time, money = map(int, ele)
    for j in range(time):
        num = 0
        while num*time + j <= t:
            dp[time*num + j] = max(dp[time*num + j], dp[j] + num*money)   
            num += 1
print(dp[t])