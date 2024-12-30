n,x = map(int,input().split())
candy = []
for i in range(n):
    a,b = map(int,input().split())
    sweet = list(a/b for _ in range(b))
    candy.extend(sweet)
candy.sort()
candy.reverse()
print("{:.1f}".format(sum(candy[0:x])))