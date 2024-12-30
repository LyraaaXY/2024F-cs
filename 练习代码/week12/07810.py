for _ in range(int(input())):
    num = input()
    if '19' in num or int(num)%19 == 0:
        print('Yes')
    else:
        print('No')