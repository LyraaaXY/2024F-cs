# n, d = map(int,input().split())
# queue = []
# for i in range(n):
#     queue.append(int(input()))
# if n == 1:
#     print(queue[0])
# else:
    
#  苏王捷 2300011075
N, D = map(int, input().split())
height = [0]*N
check = [False]*N
for i in range(N):
    height[i] = int(input())

height_new = []
while False in check:
    i, l = 0, len(height)
    buffer = []
    while i < l:
        if check[i]:
            i += 1
            continue
        if len(buffer) == 0:
            buffer.append(height[i])
            maxh = height[i]
            minh = height[i]
            check[i] = True
            continue

        maxh = max(height[i], maxh)
        minh = min(height[i], minh)
        if maxh-height[i] <= D and height[i]-minh <= D:
            buffer.append(height[i])
            check[i] = True
        i += 1
    buffer.sort()
    height_new.extend(buffer)

print(*height_new, sep='\n')
##########


##########
from collections import deque

n, d = map(int, input().split())
h = deque(int(input()) for _ in range(n))
ans = []

while h:
    inlist = []
    max_val = h[0]
    min_val = h[0]
    
    # 一次遍历完成所有必要的计算
    for _ in range(len(h)):
        height = h.popleft()
        if abs(height - max_val) <= d and abs(height - min_val) <= d:
            inlist.append(height)
        else:
            h.append(height)
        
        if height < min_val:
            min_val = height
        if height > max_val:
            max_val = height
    
    ans += sorted(inlist)

print(*ans, sep='\n')