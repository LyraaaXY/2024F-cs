#O(n**2)
n = int(input())
num = sorted(list(input().split()))
for i in range(n - 1):
    for j in range(i + 1, n):
        if num[j] + num[i] < num[i] + num[j]:
            num[i], num[j] = num[j], num[i]
mun = reversed(num)
print(''.join(mun) + ' ' + ''.join(num))

# 两倍长度是正确的。O(nlogn)
#from math import ceil
# input()
# lt = input().split()

# max_len = len(max(lt, key = lambda x:len(x)))
# lt.sort(key = lambda x: x * ceil(2*max_len/len(x)))
# lt1 = lt[::-1]
# print(''.join(lt1),''.join(lt))