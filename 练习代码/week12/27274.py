def log(n):
    count = 0
    while 2**(count + 1) <= n:
        count += 1
    return count

def array(x):
    n = log(len(x))
    want = []
    if n % 2 != 0:
        for i in range(n//2 + 1):
            want += [2**i, 2**(n - i)]
    else:
        for i in range(n//2):
            want += [2**i, 2**(n - i)]
        want += [2**(n//2)]
    begin = ''
    for i in want:
        begin += x[i - 1]
    return begin

s = input()
print(array(s))