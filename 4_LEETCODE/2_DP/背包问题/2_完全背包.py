'''
f[i][j] 前i个物品，体积为j的背包，理论上的最大价值。

f[0][0] = 0

res = max{f[N]}

f[i][j] = max{f[i-1_最短回文串.py][j], f[i-1_最短回文串.py][j-k*v[i]] + k*w[i]}

'''

N, V = map(int, input().split())

v = [0] * (N + 1)
w = [0] * (N + 1)

for i in range(1, N + 1):
    v[i], w[i] = map(int, input().split())

# print(N,V)
# print(v,w)


# f = [[0 for i in range(V+1_最短回文串.py)] for i in range(N+1_最短回文串.py)]  # 初始化全0
#
# for i in range(1_最短回文串.py, N + 1_最短回文串.py):
#     for j in range(V + 1_最短回文串.py):
#         f[i][j] = f[i - 1_最短回文串.py][j]
#         for k in range(1_最短回文串.py, j // v[i] + 1_最短回文串.py):
#             f[i][j] = max(f[i][j], f[i - 1_最短回文串.py][j - k * v[i]] + k * w[i])
#
# print(f[N][V])



# # #优化 二维数组为一维数组
# f = [0 for i in range(V+1_最短回文串.py)]  # 初始化全0
#
# for i in range(1_最短回文串.py, N + 1_最短回文串.py):
#     for j in range(V, v[i]-1_最短回文串.py, -1_最短回文串.py):
#         for k in range(0, j // v[i] + 1_最短回文串.py):
#             f[j] = max(f[j], f[j - k * v[i]] + k * w[i])
#
# print(f[V])



#优化  取消k
f = [0 for i in range(V+1)]  # 初始化全0

for i in range(1, N + 1):
    for j in range(v[i], V+1):
            f[j] = max(f[j], f[j-v[i]] + w[i])

print(f[V])