number = int(input())
n=0
for i in range(number):
    a,b,c = [int(s) for s in input().split()]
    if a + b + c > 1:
        n += 1
print(n)