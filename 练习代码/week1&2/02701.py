n = int(input())
result=[]
for i in range(n+1):
    if i%10 != 7 and i%7 != 0 and i//10 != 7:
        result.append(i**2)
print(sum(result))