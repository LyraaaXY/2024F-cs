def find(b, k):
    max_v, count = nums[b], b
    for i in range(b + 1, b + k):
        if nums[i] >= max_v:
            max_v, count = nums[i], i
    return max_v, count

n, k = map(int, input().split())
nums = list((map(int, input().split())))
if k == 1:
    print(' '.join(map(str, nums)))
else:    
    res = [0]*(n - k + 1)
    max_v, count = - float('inf'), -1
    for i in range(n - k + 1):
        if count < i:
            max_v, count = find(i, k)
        else:
            if nums[i + k - 1] >= max_v:
                max_v, count = nums[i + k - 1], i + k - 1
        res[i] = max_v
    print(' '.join(map(str, res)))