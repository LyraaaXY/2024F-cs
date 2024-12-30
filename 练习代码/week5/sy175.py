# personal tle
# n, k = map(int, input().split())
# rec = list(map(int, input().split()))
# count = 0
# for i in range(n - 1):
#     flag = True
#     j = n - 1
#     while flag == True and i < j < n:
#         if rec[i] + rec[j] == k:
#             count += 1
#             flag = False
#         j -= 1
# print(count)

#official
def two_sum_pairs(n, k, A):
    count = 0  # 初始化计数器
    i, j = 0, n - 1  # 初始化双指针
    
    while i < j:
        if A[i] + A[j] == k:
            count += 1  # 找到一个满足条件的对
            i += 1  # 右移左指针
            j -= 1  # 左移右指针
        elif A[i] + A[j] < k:
            i += 1  # 右移左指针以增大和
        else:
            j -= 1  # 左移右指针以减小和
    
    return count

# 读取输入
n, k = map(int, input().split())
A = list(map(int, input().split()))

# 输出结果
print(two_sum_pairs(n, k, A))