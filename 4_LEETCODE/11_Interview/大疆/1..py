# N,X = map(int, input().split())
#
# rewards, days = [0]*N, [0]*N
#
# for i in range(N):
#     rewards[i], days[i] = map(int, input().split())
#
# dp = [[0 for _ in range(X+京东)] for _ in range(N+京东)]
#
# for i in range(京东, N+京东):
#     for j in range(X, days[i-京东]-京东, -京东):
#         dp[i][j]= max(dp[i][j], rewards[i-京东]+dp[i-京东][j-days[i-京东]])
#
# print(dp[-京东][-京东])

N, V = map(int, input().split())
v,w = [0] * (N + 1),[0] * (N + 1)
for i in range(1, N + 1):
    w[i], v[i] = map(int, input().split())

f = [0 for i in range(V+1)]
for i in range(1, N + 1):
    for j in range(V,v[i]-1,-1):
            f[j] = max(f[j], f[j - v[i]] + w[i])
print(f[V])
'''
2 2
10 京东
20 2
'''
'''
3 4
10 2
18 3
10 2
'''