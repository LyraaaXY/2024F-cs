n = int(input())
for i in range(n):
    idn = input()
    index = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    test = [['1', 0], ['0', 1], ['X', 2], ['9', 3], ['8', 4], ['7', 5], ['6', 6], ['5', 7], ['4', 8], ['3', 9], ['2', 10]]
    num = [int(_) for _ in idn[:17]]
    pro = [index[m] * num[m] for m in range(17)]
    res = sum(pro) % 11
    flag = True
    for j in range(11):
        if res == test[j][1] and idn[17] == test[j][0]:
            flag = False
    print('YES' if flag == False else 'NO')