def judge(x):
    if x == 0:
        return 0
    else:
        return x//abs(x)

n = int(input())
nums = list(map(int,input().split()))
change = [judge(nums[i+1]-nums[i]) for i in range(n-1)]

result = 1
pre = 0
for i in range(n-1):
    if (pre == 0 and change[i] != 0) or change[i]*pre < 0:
        result += 1
        pre = change[i]
print(result)