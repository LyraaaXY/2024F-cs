def cmp(D, P, n):
    D_s = sorted(D)
    P_s = sorted(P)
    if n%2 == 0:
        return (D_s[n//2 - 1] + D_s[n//2])/2, (P_s[n//2 - 1] + P_s[n//2])/2
    else:
        return D_s[n//2], P_s[n//2]
    
n = int(input())
data = list(input().split())
P = list(map(int, input().split()))
D = []
for i in range(n):
    x, y = map(int, data[i][1:-1].split(','))
    D.append((x + y)/P[i])
D_m, P_m = cmp(D, P, n)
count = 0
for i in range(n):
    if D[i] > D_m and P[i] < P_m:
        count += 1
print(count)