n = int(input())
trees = []
for i in range(n):
    trees.append(list(map(int, input().split())))
count = 2
if n == 1:
    print(1)
else:
    for i in range(1, n - 1):
        if trees[i][0] - trees[i][1] > trees[i - 1][0]:
            count += 1
        elif trees[i][0] + trees[i][1] < trees[i + 1][0]:
            count += 1
            trees[i][0] += trees[i][1]
    print(count)