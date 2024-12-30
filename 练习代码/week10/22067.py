real, pro = [], []

while True:
    try:
        act = input().split()
        if act[0] == "pop":
            if real:
                real.pop()
                if pro:
                    pro.pop()
        elif act[0] == "min":
            if pro:
                print(pro[-1])
        else:
            num = int(act[1])
            real.append(num)
            if not pro or pro[-1] >= num:
                pro.append(num)
            else:
                pro.append(pro[-1])
    except EOFError:
        break