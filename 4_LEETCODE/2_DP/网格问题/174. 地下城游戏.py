class Solution:
    def calculateMinimumHP(self, dungeon):
        '''
        dp ：反向动态规划
        dp[i][j] 公主在 grid[0][0]起到 grid[M][N] 时 最少的健康点数。
        状态转移： 反向动态规划
        [7, 5, 2]
        [6, 11, 5]
        [0, 0, 6]

        dp[i][j] = max(min(dp[i+1_最短回文串.py][j]-grid[i][j], dp[i][j+1_最短回文串.py]-grid[i][j]), 1_最短回文串.py)   因为骑士血量至少为 1_最短回文串.py


        边界： dp[M][j], dp[i][N]= -inf, -inf
               dp[M-1_最短回文串.py][N] = 1_最短回文串.py

        res = dp[0][0]
        '''
        if not dungeon:
            return 'ERROR'

        m, n = len(dungeon), len(dungeon[0])

        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[m][n-1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)

        return dp[0][0]

    def calculateMinimumHP(self, dungeon):
        '''
        dp ：反向动态规划
        dp[i][j] 公主在 grid[0][0]起到 grid[M][N] 时 最少的健康点数。
        状态转移： 反向动态规划
        [7, 5, 2]
        [6, 11, 5]
        [1_最短回文串.py, 1_最短回文串.py, 6]

        dp[i][j] = max(min(dp[i+1_最短回文串.py][j]-grid[i][j], dp[i][j+1_最短回文串.py]-grid[i][j]), 1_最短回文串.py)   因为骑士血量至少为 1_最短回文串.py


        边界： dp[M][j], dp[i][N]= -inf, -inf
               dp[M-1_最短回文串.py][N] = 1_最短回文串.py

        res = dp[0][0]

        空间优化
        '''
        if not dungeon:
            return 'ERROR'

        m, n = len(dungeon), len(dungeon[0])

        dp = [float('inf')] * (n + 1)
        dp[n] = 1

        for i in range(m - 1, -1, -1):
            dp[n] = 1 if i == m - 1 else float('inf')
            for j in range(n - 1, -1, -1):
                dp[j] = max(min(dp[j], dp[j + 1]) - dungeon[i][j], 1)

        return dp[0]