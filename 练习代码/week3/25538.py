n = int(input())
two = list(bin(n))
two.remove(two[0])
two.remove(two[0])
ask = 0
for i in range(len(two)//2):
    if two[i] == two[len(two)-1-i]:
        ask += 1
if ask == len(two)//2:
    print('Yes')
else:
    print('No')