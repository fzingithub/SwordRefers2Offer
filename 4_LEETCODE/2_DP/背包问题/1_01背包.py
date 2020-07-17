N, V = map(int, input().split())  # 物品数， 背包容量

v = [0] * (N + 1)  # 体积 索引从1开始到n
w = [0] * (N + 1)  # 价值 索引从1开始到n

for i in range(1, N + 1):
    v[i], w[i] = map(int, input().split())

# f = [[0 for i in range(V+1)] for i in range(N+1)]  # 初始化全0
#
#
# for i in range(1, N + 1):
#     for j in range(V + 1):
#         f[i][j] = f[i - 1][j]
#
#         if j >= v[i]:
#             f[i][j] = max(f[i][j], f[i - 1][j - v[i]] + w[i])
#
# print(f[N][V])

# 4 5
# 1 2
# 2 4
# 3 4
# 4 5



# 空间优化
f = [0 for i in range(V+1)]  # 初始化全0

for i in range(1, N + 1):
    for j in range(V, -1, -1):
        if j>=v[i]:
            f[j] = max(f[j], f[j - v[i]] + w[i])

print(f[V])