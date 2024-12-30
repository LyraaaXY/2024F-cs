pell = [1,2]
for i in range(2,1000000):
    pell.append((pell[i-2]+2*pell[i-1])%32767)

n = int(input())
for j in range(n):
    num = int(input())
    print(pell[num-1])