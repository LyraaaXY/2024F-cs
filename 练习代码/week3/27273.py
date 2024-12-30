n = int(input())

for i in range(n):
    num= int(input())
    # time exceeded version
    #j = 0
    #add = []
    #for k in range(1, num + 1):
    #    if k % 2**j == 0:
    #        add.append(-k)
    #        j += 1
    #    else:
    #        add.append(k)
    #print(sum(add))

    #standard version
    j = 0
    while 2**j <= num:
        j += 1
    ans = int((num + 1)*num/2 -2**(j+1) +2)
    print(ans)