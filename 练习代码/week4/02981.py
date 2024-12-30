a = input()
a = (201 - len(a))*['0'] + list(a)
b = input()
b = (201 - len(b))*['0'] + list(b)
c = 201*['0']
for i in range(200,0,-1):
    c[i] = int(a[i]) + int(b[i]) + int(c[i])
    if c[i] >= 10:
        c[i] -= 10
        c[i-1] = '1'
    c[i] = str(c[i])
while c[0] == '0':
    c.remove(c[0])
print(''.join(c))