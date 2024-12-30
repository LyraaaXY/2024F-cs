n = int(input())

for i in range(n):
    data = input()
    year = int(data[ :4])
    m = int(data[4:6])
    d = int(data[6: ])
    if m < 3:
        year -= 1
        m += 12
    c = int(str(year)[ :2])
    y = int(str(year)[2:4])
    calendar = (y + c//4 + y//4 - 2*c + (26*(m+1))//10 + d -1) % 7
    d = {0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
    print(d[calendar])