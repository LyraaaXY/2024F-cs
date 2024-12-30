n = int(input())
kingl, kingr = map(int, input().split())
data = []
for i in range(n):
    left, right = map(int, input().split())
    data.append([left, right])
data.sort(key = lambda x:x[0]*x[1])
count = kingl
money = [count//data[0][1]]
for i in range(1, n):
    count *= data[i - 1][0]
    money.append(count//data[i][1])
print(max(money))