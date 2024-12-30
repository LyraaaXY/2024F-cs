h = int(input())
m = int(input())
t = 2*h - 0.5*m
classes = []
score = 0
for i in range(m):
    classes.append(list(map(float, input().split())))
classes.sort(key = lambda x:(x[0]*x[1],x[0]))
classes.reverse()
for i in range(m):
    if 5/classes[i][0] > t:
        score += t*classes[i][0]*classes[i][1]
        break
    else:
        score += 5*classes[i][1]
        t -= 5/classes[i][0]
print(f"{score:.1f}")