def queen(n):
    if n == 1:
        return ['1', '2', '3', '4', '5', '6', '7', '8']
    else:
        array = []
        for ele in queen(n - 1):
            minus = [int(ele[i]) - i  for i in range(n - 1)]
            plus = [int(ele[i]) + i for i in range(n - 1)]
            for item in queen(1):
                if item not in ele and int(item) + n - 1 not in plus and int(item) - n + 1 not in minus:
                    array.append(ele + item)
        return array

ans = sorted(queen(8))
for _ in range(int(input())):
    print(ans[int(input()) - 1])