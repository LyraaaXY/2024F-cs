n = int(input())
ans = []
for i in range(n):
    string = ''
    num = int(input())
    count = 1
    while len(string) < num:
        string += str(count)
        num -= len(string)
        count += 1
    ans.append(string[num - 1])
print('\n'.join(ans))