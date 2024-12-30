repr = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
n,k = map(int,input().split())
ans = ['']*11
for j in range(10,-1,-1):
    num = n//k**j
    n -= num*(k**j)
    if num != 0 or j < 10 and ans[9-j] != '':
        ans[10-j] = repr[num]
print(''.join(ans))
