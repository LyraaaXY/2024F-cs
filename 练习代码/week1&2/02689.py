string = input()
ori = list(string)
low = list(string.lower())
up = list(string.upper())
result = []
for i in range(len(string)):
    if ori[i] == low[i]:
        result.append(up[i])
    else:
        result.append(low[i])
print(''.join(result))