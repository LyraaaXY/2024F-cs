tab = [i for i in input()]
vowel = ['a','o','e','i','u','y']
res = []
for str in tab:
    if str not in vowel:
        res.append('.')
        res.append(str)
print(''.join(res))