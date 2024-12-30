n = int(input())
stu = list(map(int, input().split()))
stus = [[i + 1, stu[i]] for i in range(n)]
stus.sort(key = lambda x:(x[1], x[0]))
time = sum([(n - i - 1)*stus[i][1] for i in range(n)])/n
print(' '.join([str(stus[i][0]) for i in range(n)]))
print(f'{time:.2f}')