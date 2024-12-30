nb = int(input())
boys = sorted(list(map(int,input().split())))
ng = int(input())
girls = sorted(list(map(int,input().split())))
pair = 0
for i in range(nb):
    for j in range(ng):
        if abs(boys[i] - girls[j]) <= 1:
            girls[j] = 10**4
            pair += 1
            break
print(pair)