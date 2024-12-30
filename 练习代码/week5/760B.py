# TLE set.ver
# n = int(input())
# price = sorted(list(map(int, input().split())))
# q = int(input())
# for i in range(q):
#     money = int(input())
#     if money >= max(price):
#         print(n)
#     elif money < price[0]:
#         print(0)
#     else:
#         flag = True
#         tries = 0
#         while tries < n and flag == True:
#             if money < price[tries]:
#                 print(tries)
#                 flag = False
#             tries += 1

# erfenchazhao
n = int(input())
shop = sorted(list(map(int,input().split())))
m = int(input())
for i in range(m):
    a = int(input())
    l = 0
    r = n-1
    while l<=r:
        mid = (l+r)//2
        if a < shop[mid]:
            r = mid-1
        elif a >= shop[mid]:
            l = mid + 1
    print(r+1)