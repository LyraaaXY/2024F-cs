t = int(input())
for i in range(t):
    n, x =  map(int, input().split())
    array = list(map(int, input().split()))
    while array != []:
        if sum(array)%x != 0:
            print(len(array))
            break
        else:
            if array[0]%x != 0 or array[0]%x == 0 and array[len(array) - 1]%x == 0:
                array.remove(array[0])
            else:
                array.pop()
    if array == []:
        print(-1)