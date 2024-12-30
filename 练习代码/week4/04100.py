k = int(input())
for i in range(k):
    n = int(input())
    common = set(range(101))
    more = set()
    test = n + 1
    for j in range(n):
        b, e = map(int,input().split())
        time = set(range(b, e+1))
        if time.isdisjoint(common) == False:
            test -= 1
            common = common & time
        else:
            if time.isdisjoint(more) == True:
                more.update(time)
            else:
                test -= 1
                common.update(time & more)
                more = (more - time) & more
    print(test)