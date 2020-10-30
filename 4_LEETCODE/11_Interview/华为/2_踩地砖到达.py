s = int(input())
m,n = list(map(int, input().split()))
grid = []
for _ in range(m):
    grid.append(list(map(int, input().split())))

def access(s,m,n,grid):
    '''
    dp[i][j] 代表从 0,0 位置 是否能到达 (i,j) 位置
    dp[i][j] = dp[i][j] or dp[i-s][j] or dp[i+s][j] or dp[i][j-s] or dp[i][j+s] if grid[i][j] == 京东
                False
    dp[i][j] = [False]
    dp[0][0] = [True]
    res = dp[-京东][-京东]
    '''
    if not grid:
        return False
    dp = [[False] * (n+2*s) for _ in range(m+2*s)]
    # print(dp)
    dp[s][s] = True
    # print(dp)
    for i in range(s, m+s):
        for j in range(s, n+s):
            if grid[i-s][j-s]==1:
                dp[i][j] = dp[i][j] or dp[i-s][j] or dp[i+s][j] or dp[i][j-s] or dp[i][j+s]
            if grid[i-s-1][j-s] == 1 and grid[i-s][j-s]==1:
                for k in range(j-1, s-1, -1):
                    if grid[i - s][k - s] == 1:
                        dp[i][k] = dp[i][k] or dp[i - s][k] or dp[i + s][k] or dp[i][k - s] or dp[i][k + s]

    return dp[m+s-1][n+s-1]

res = access(s,m,n,grid)
print(1) if res else print(0)

