import math

n = int(input())
teams = input().split()
t_1, t_2, t_3, t_4 = teams.count('1'), teams.count('2'), teams.count('3'), teams.count('4')
res = t_4 + t_3 + math.ceil(t_2/2)
if t_1 > t_3 + 2*(math.ceil(t_2/2) - math.floor(t_2/2)):
    res += math.ceil((t_1 - (t_3 + 2*(math.ceil(t_2/2) - math.floor(t_2/2))))/4)
print(res)