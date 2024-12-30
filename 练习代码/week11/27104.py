# 数院胡睿诚					time: 897ms
# 就是从左往右扫，一轮一轮的扫

# 比如现在这一轮结束之后第一个没被盖住的是x,你就继续扫能盖住x的，
# 在所有能盖住x的里面挑右端点最靠右边的，把它选进来，然后更新第一个没被盖住的点，进入下一轮
#
# 其实这个算法对于任给一族区间要找最小覆盖的问题都对

N = int(input())
a = list(map(int, input().split()))
intervals = [(max(0, i-a[i]), min(N-1, i+a[i])) for i in range(N)]
intervals.sort()

ans = 0
right = 0
temp = -1
index = 0
while index < N and right < N:
    while index < N and intervals[index][0] <= right:
        temp = max(temp, intervals[index][1])
        index += 1
    right = temp + 1
    ans += 1

print(ans)