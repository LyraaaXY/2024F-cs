n = int(input())
entity = 0
for i in range(n):
    ask = input().replace('### ###',' ')
    result = ask.count('###')//2
    entity += result
print(entity)    