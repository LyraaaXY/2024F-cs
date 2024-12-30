n = int(input())
def F(n, f, m, b):
    if n == 0:
        return []
    else:
        return F(n - 1, f, b, m) + [f + '->' + b] + F(n - 1, m, f, b)
print(2**n - 1)
print('\n'.join(F(n, 'A', 'B', 'C')))