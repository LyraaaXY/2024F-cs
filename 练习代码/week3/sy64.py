n = int(input())
num = list(map(int,input().split()))
k = int(input())
pro = [(k - i) for i in num]
count = 0
for j in range(n):
    if num[j] in pro:
        count += 1
print(count//2)