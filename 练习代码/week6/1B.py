n = int(input())
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
for i in range(n):
    string = input()
    if string[0] == 'R' and string[1] in num and 'C' in string:
        row = ''
        string = string[1:]
        while string[0] in num:
            row = row + string[0]
            string = string[1:]
        pro = int(string[1:])
        column = ['']*5
        for i in range(5):
            if pro == 0:
                break
            if pro%26 == 0:
                column[i] = 'Z'
                pro = pro//26 - 1
            else:
                column[i] = chr(pro%26 + 64)
                pro = (pro - pro%26)//26
        column.reverse()
        column = ''.join(column)
        print(column + row)
    else:
        column = []
        while string[0] not in num:
            column.append(ord(string[0]) - 64)
            string = string[1:]
        column_1 = sum([column[num]*(26**(len(column) - num - 1)) for num in range(len(column))])
        print('R' + string + 'C' + str(column_1))