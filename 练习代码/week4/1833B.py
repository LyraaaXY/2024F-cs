# t = int(input())
# for _ in range(t):
#     n, k = map(int,input().split())
#     a = list(map(int,input().split()))
#     b = list(map(int,input().split()))
#     b_r =[]
#     for i in range(n):
#         for j in range(n):
#             if abs(a[i] - b[j]) <= k:
#                 b_r.append(b[j])
#                 b[j] = 10**9 + k + 1
#     print(' '.join([str(num) for num in b_r]))

#right answer doesn't take k into consideration and just sort the two tables instead
t = int(input())
for _ in range(t):
    j, k = map(int, input().split())

    l1 = list(map(int, input().split()))
    v = [(l1[i], i) for i in range(j)]
    v.sort()

    l2 = list(map(int, input().split()))
    l2.sort()

    z = [0] * j
    for i in range(j):
        z[v[i][1]] = l2[i]

    for data in z:
        print(data, end=" ")
    print()