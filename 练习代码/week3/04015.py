while True:
    try:
        email = input()
        if email.count('@') == 1:
            a, b = email.split('@')
            if a != '' and b != '' and b.count('.') > 0 and a[0] != '.' and a[-1] != '.' and b[0] != '.' and b[-1] != '.':
                    print('YES')
            else:
                print('NO')
        else:
            print('NO')
    except EOFError:
        break