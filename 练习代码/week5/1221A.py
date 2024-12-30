q = int(input())
for i in range(q):
    n = int(input())
    nums = list(map(int,input().split()))
    if 2048 in nums:
        print('YES')
    elif sum(nums) < 2048:
        print('NO')
    else:
        count = [0]*12
        for j in range(n):
            flag = True
            k = 0
            while k < 11 and flag == True:
                if nums[j] == 2**k:
                    count[k] += 1
                    flag = False
                k += 1
        for m in range(11):
            while count[m] > 1:
                count[m] -= 2
                count[m + 1] += 1
        print('YES' if count[11] > 0 else 'NO')