n = int(input())
pair = []
for i in range(n):
    a,b = map(int,input().split())
    pair.append([a,b])
pair_1 = sorted(pair,key = lambda x:(x[0],x[1]))
pair_2 = sorted(pair,key = lambda x:(x[1],x[0]))
print('Poor Alex' if pair_1 == pair_2 else 'Happy Alex')