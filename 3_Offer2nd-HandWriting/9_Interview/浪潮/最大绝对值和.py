# n = int(input())
#
# data = []
# for i in range(n):
#     data.append(int(input()))

'''
要想到b数组那个差值最大，要么是1要么是ai。

1. 状态定义：
dp[i][0]代表第i个取得1，dp[i][1]代表第i个取得ai值。

2. 边界：
dp[0][0] = 0, dp[0][1] = 0
dp[1][0] = 0, dp[1][1] = 0

3.状态转移：
dp[i][0] = max(dp[i-1][0], dp[i-1][1]+abs(1- data[i-2]))
dp[i][1] = max(dp[i-1][0]+abs(data[i-1]-1), dp[i-1][1] + abs(data[i-1]-data[i-2]))

4. 结果
res = max(dp[n][0],dp[n][1])
'''
data = [10, 1, 10, 1, 10]
n = len(data)

dp = [[0] *2 for _ in range(n+1)]

for i in range(2, n+1):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1]+abs(1- data[i-2]))
    dp[i][1] = max(dp[i-1][0]+abs(data[i-1]-1), dp[i-1][1] + abs(data[i-1]-data[i-2]))

print(dp)
print(max(dp[-1][0], dp[-1][1]))