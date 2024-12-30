t = int(input())
num = 0
for i in range(1, t):
    flag = True
    if num < i and flag:
        flag = False
    num += 1
    print(num)