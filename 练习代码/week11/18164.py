import heapq

n = int(input())
length = list((map(int, input().split())))
heapq.heapify(length)
cut = 0
for i in range(n - 1):
    x1 = heapq.heappop(length)
    x2 = heapq.heappop(length)
    x = x1 + x2
    heapq.heappush(length, x)
    cut += x
print(cut)