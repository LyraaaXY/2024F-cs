begin, end, n = input().split()
b_h, b_m = map(int, begin.split(':'))
e_h, e_m = map(int, end.split(':'))
time  = (e_h - b_h)*60 + e_m - b_m
dp = [0]*(time + 1)
t_l, t_ul = [], []
for i in range(int(n)):
    t, c, p = map(int, input().split())
    if p == 0:
        t_ul.append((t, c))
    else:
        t_l.append((t, c, p))
for trees in t_l:
    t, c, p = trees
    for j in range(1, p + 1):
        for i in range(time, min(j*t, time) - 1, -1):
            dp[i] = max(dp[i], dp[i - j*t] + c*j)
for trees in t_ul:
    t, c = trees
    for i in range(time + 1):
        if (i == 0 or dp[i] != 0) and i + t <= time:
            dp[i + t] = max(dp[i] + c, dp[i + t])
print(dp[t])