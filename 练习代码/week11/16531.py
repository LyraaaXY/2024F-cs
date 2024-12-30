import bisect
D = [[1, 0], [0, 1], [-1, 0], [0, -1]]
def same(data):
    count = 0
    for i in range(m):
        for j in range(n):
            flag = True
            for ele in D:
                if 0 <= i + ele[0] < m and 0 <= j + ele[1] < n and data[maps[i][j]] == data[maps[i + ele[0]][j + ele[1]]]:
                    flag = False
            if not flag:
                count += 1
    return count

def judge(grade, t):
    grade.sort()
    count, ans  = 0, grade[0]
    while bisect.bisect_right(grade, ans) <= t:
        count = bisect.bisect_right(grade, ans)
        ans = grade[count]
    return count

m, n = map(int, input().split())
maps = []
for _ in range(m):
    maps.append(list(map(int, input().split())))
great = int(m*n*0.4)
data, grade = [], []
for _ in range(m*n):
    a = input()
    data.append(a)
    grade.append(-sum(list(map(int, a.split()))))
print(same(data), judge(grade, great))