for _ in range(int(input())):
    full = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'}
    fake, heavy, light = full, set(), set()
    for i in range(3):
        a, b, status = input().split()
        a, b = {num for num in a}, {num for num in b}
        if status == 'even':
            fake = fake - a - b
        elif status == 'up':
            fake = (a|b)&fake
            heavy = heavy|a
            light = light|b
        else:
            fake = (a|b)&fake
            heavy = heavy|b
            light = light|a
    coin = fake.pop()
    if coin in heavy:
        print(coin + ' is the counterfeit coin and it is heavy.')
    else:
        print(coin + ' is the counterfeit coin and it is light.')              