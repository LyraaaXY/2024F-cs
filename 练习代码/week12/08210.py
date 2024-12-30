l, n, m  = map(int, input().split())
stones = [0]
for i in range(n):
    stones.append(int(input()))
stones.append(l)

def remove(l, m):
    count, d = 0, 0
    for i in range(1, n + 2):
        if stones[i] - d < l:
            count += 1
        else:
            d = stones[i]
    return count > m

left, right = 0, l + 1
while left < right:
    mid = (left + right)//2
    if remove(mid, m):
        right = mid
    else:
        ans = mid
        left = mid + 1
print(ans)