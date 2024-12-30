long = input().lower()
short = []
n = 1
pre = long[0]
for i in range(len(long)):
    if long[i] == pre:
        n += 1
    else:
        short.append('('+pre+','+str(n)+')')
        pre = long[i]
        n = 1
short.append('('+pre+','+str(n)+')')
print(''.join(short))