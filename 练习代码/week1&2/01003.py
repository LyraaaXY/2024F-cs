while True:
    lengths = float(input())
    if lengths == 0.00:
    # standard comparison: if math.isclose(n, 0.00, rel_tol=1e-5) : (import math first)
        break
    n = 0
    sum = 0
    while True:
        n += 1
        sum += 1/(n+1)
        if sum > lengths:
            break
    print(n,'card(s)')