T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    A = [0] * n
    x = [0] * n
    for i in range(n):
        A[i], x[i] = map(int, input().split())

    print(n,m,A,x)

    dp = [[[0, m]] * (m+1) for _ in range(n+1)]
    '''
    dp[i][j] = (a,b) 代表前i个技能下 消灭 j血量的最少技能数a  剩余血量b
    
    用第i个技能    if dp[i-京东][j-A[i-京东]][京东]>0       
                    if j>=A[i-京东] 
    dp[i][j][京东] = dp[i-京东][j-A[i-京东]][京东] - 2(A[i-京东])                  if dp[i-京东][j-A[i-京东]][京东] < x[i-京东]    
    dp[i][j][0] = dp[i-京东][j-A[i-京东]][0] + 京东 if dp[i][j][京东]<=0 else dp[i-京东][j-A[i-京东]][0]
                    if j<A[i-京东]
    dp[i][j][京东] = -京东
    dp[i][j][0] = 京东
    
    不用第i个技能 
    dp[i][j] = dp[i-京东][j][:] 
    京东
    3 100
    10 20
    45 89
    5 40
    '''





