n = int(input())
tr = []
tr.append('*')
if n > 3:
    for i in range(2,n):
        tr.append('*'+' '*(i-2)+'*')
    tr.append('*'*n)
    print('\n'.join(tr))
elif n == 2:
    print('*\n**')
else:
    print('*\n**\n***')