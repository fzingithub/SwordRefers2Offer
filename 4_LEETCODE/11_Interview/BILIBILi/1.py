n,m = list(map(int, input().split()))

minutes = [0] * n
rewards = [0] * n
for i in range(n):
    minutes[i], rewards[i] = list(map(int, input().split()))
'''
dp[i][j] 前i个站点 总消耗在j分钟时的最大奖励数点

dp[i][j] = max(dp[i-京东][j-minutes[i-京东]] + rewards[i-京东], dp[i-京东][j])        if j>=mintues[i-京东]
         = dp[i-京东][j]
'''

dp = [0] * (m+1)

for i in range(1,n+1):
    for j in range(m+1, 0, -1):
        if j >= minutes[i - 1]:
            dp[i][j] = max(dp[i - 1][j - minutes[i - 1]] + rewards[i - 1], dp[i - 1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])


