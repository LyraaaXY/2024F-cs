def rotate(x):
    rotate = []
    for i in range(len(x)):
        rotate.append(int(x[i:] + x[:i]))
    return rotate
while True:
    try:
        rec = input()
        num = int(rec)
        flag = True
        for i in range(2,len(rec) + 1):
            if i*num not in rotate(rec):
                flag = False
                break
        print(rec + ' is cyclic' if flag == True else rec + ' is not cyclic' )
    except EOFError:
        break