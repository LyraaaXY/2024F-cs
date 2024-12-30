n, m = map(int,input().split())
total = []
for i in range(2):
    total += list(map(int, input().split()))
print(' '.join(map(str,(sorted(total)))))