import math

def square(y):
    x = int(y)
    if x != 0 and math.sqrt(x) == int(math.sqrt(x)):
        return True
    
def div(x):
    if square(x):
        return True
    for i in range(1, len(x)):
        if square(x[: - i]):
            if div(x[len(x) - i:]):
                return True
            else:
                continue
print('Yes' if div(input()) else 'No')