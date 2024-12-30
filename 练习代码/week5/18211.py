p = int(input())
cost = sorted(list(map(int, input().split())))
w_m = 0
w_e = 0
total = len(cost)
while w_m + w_e < total:
    if cost[0] <= p:
        p -= cost[0]
        w_m += 1
        cost.remove(cost[0])
    else:
        if w_m > w_e and len(cost) > 1:
            p += max(cost)
            w_e += 1
            cost.pop()
        else:
            break
print(w_m - w_e)