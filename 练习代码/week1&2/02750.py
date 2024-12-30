feet=int(input())
head_max=feet//2
head_min=feet//4  #a//b=int(a/b)
if feet%2 == 0:
    if feet%4 == 0:
        print(str(head_min)+' '+str(head_max))
        #print('{} {}'.format(head_min,head_max))  --by official answer
        #print(f'{head_min} {head_max}')  --by yyx
        #print("%d %d" % (head_min,head_max))  #--by yyx
    else:
        print(str(head_min+1)+' '+str(head_max))
else:
    print('0 0')