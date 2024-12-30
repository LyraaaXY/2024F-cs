import math

T_prime = []
number = [False]*2 + [True]*999999
for j in range(2,1000001):
    if number[j] == True:
        T_prime.append(j**2)
        for k in range(2, 1000000//j + 1):
            number[k*j] = False 
    
n = int(input())
rec = list(map(int, input().split()))
ans = []
for i in range(n):
    if rec[i] < 4 or int(rec[i]**0.5) != rec[i]**0.5:
        ans.append('NO')
    elif rec[i] in T_prime:
        ans.append('YES')
    else:
        ans.append('NO')
print('\n'.join(ans))