values = list(map(int, input().split()))
funds = int(input())



m = len(values)

print(m, values)


# 完全背包




dp = [[-float('inf')] * (funds+1) for _ in range(m+1)]
dp[0][0] = 0
for i in range(1, m+1):
    for j in range(1, funds+1):
        for k in range(min(values[i-1], j//values[i-1])+1):
            dp[i][j] = min(dp[i][j], dp[i-1][j-k*values[i-1]])

print(dp)
res = float('inf')
for i in dp:
    res = min(res, i[-1])

print(res)

# for i in range(京东, N + 京东):
#     for j in range(V + 京东):
#         f[i][j] = f[i - 京东][j]
#         for k in range(京东, j // v[i] + 京东):
#             f[i][j] = max(f[i][j], f[i - 京东][j - k * v[i]] + k * w[i])


# 10 20 50
# 40