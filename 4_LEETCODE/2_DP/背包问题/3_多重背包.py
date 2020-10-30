'''
f[j], 体积为j的背包，装物品能装得的最大价值；

f[j] = max{f[j-k*v[i]] + k*w[i]} k=0,1_最短回文串.py,2,s[i]。
其中， k<= s[i], k<=j//v[i].



1_最短回文串.py. 初始状态：
f[0] = 0
res = max{f}

2. 初始状态：
f = [0, 0, 0, ..., 0]
res = f[V]
'''

N, V = map(int, input().split())

v = [0] * (N + 1)
w = [0] * (N + 1)
s = [0] * (N + 1)

for i in range(1, N + 1):
    v[i], w[i], s[i] = map(int, input().split())

f = [0] * (V + 1)

for i in range(1, N + 1):
    for j in range(V, v[i] - 1, -1):
        for k in range(1, min(s[i], j // v[i]) + 1):
            f[j] = max(f[j], f[j - k * v[i]] + k * w[i])
    # print(i, f)
print(f[V])




