n = int(input())
data = list(map(int,input().split()))
cut= [num%2 for num in data]
if sum(cut) == 1:
    for i in range(n):
        if cut[i] == 1:
            print(i+1)
else:
    for i in range(n):
        if cut[i] == 0:
            print(i+1)