n = int(input())
price = list(map(int,input().split()))
ecirp = sorted(price)
m = int(input())
for i in range(m):
     t,l,r = map(int,input().split())
     if t == 1:
         print(sum(price[l-1:r]))
     else:
         print(sum(ecirp[l-1:r]))

# # 输入数据  
# n = int(input())  
# price = list(map(int, input().split()))  
# ecirp = sorted(price)  
  
# # 构建原始价格和排序后价格的前缀和数组  
# prefix_sum_price = [0] * (n + 1)  
# prefix_sum_ecirp = [0] * (n + 1)  
# for i in range(1, n + 1):  
#     prefix_sum_price[i] = prefix_sum_price[i - 1] + price[i - 1]  
#     prefix_sum_ecirp[i] = prefix_sum_ecirp[i - 1] + ecirp[i - 1]  
  
# # 输入查询数量  
# m = int(input())  
  
# # 处理查询  
# for _ in range(m):  
#     t, l, r = map(int, input().split())  
#     l -= 1  # 调整为0索引  
#     r -= 1  # 调整为0索引的结束位置（包含在内）  
#     if t == 1:  
#         # 使用前缀和数组计算原始价格的区间和  
#         print(prefix_sum_price[r + 1] - prefix_sum_price[l])  
#     else:  
#         # 使用前缀和数组计算排序后价格的区间和  
#         print(prefix_sum_ecirp[r + 1] - prefix_sum_ecirp[l])