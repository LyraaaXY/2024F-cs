n,m,a = input().split()
n = int(n)
m = int(m)
a = int(a)
n1 = n//a
m1 = m//a
if n%a == 0 and m%a == 0:
    print(n1*m1)
elif n%a != 0 and  m%a == 0:
    print((n1+1)*m1)
elif n%a == 0 and m%a != 0:
    print(n1*(m1+1))
else:
    print((n1+1)*(m1+1))