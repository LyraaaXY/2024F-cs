def lucky(n):
    test = set(int(i) for i in str(n))
    if n%4 != 0 and n%7 != 0 and test.union({4,7}) != {4,7}:
        return False
    else:
        return True

def llucky(n):
    t = 0
    for i in range(2,n+1):
        if lucky(i) == True:
            if n%i == 0:
                t += 1
    if t > 0:
        return True
    else:
        return False
    
num = int(input())
print('YES' if llucky(num) == True else 'NO')