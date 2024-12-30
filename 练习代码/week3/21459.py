n = int(input())
x = n
while x > 1:
    if x%2 == 0:
        x = x//2
        print('%d/2=%d'%(2*x,x))
    else:
        x = 3*x +1
        print('%d*3+1=%d'%((x-1)//3,x))