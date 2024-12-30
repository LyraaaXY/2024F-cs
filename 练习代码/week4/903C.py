from collections import Counter
n = int(input())
boxes = list(map(int,input().split()))
print(max(Counter(boxes).values()))