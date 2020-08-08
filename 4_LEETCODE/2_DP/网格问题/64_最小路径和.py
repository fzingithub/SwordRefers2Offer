class Solution:
    def minPathSum(self, grid):
        '''
        dp[i][j] 代表 （0,0）->（i-1.j-1） 最短路径

        dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i-1][j-1]

        dp[0][j] = inf
        dp[i][0] = inf
        dp[0][1] = 0

        res = dp[-1][-1]
        '''
        if not grid:
            return -1

        if grid and not isinstance(grid[0], list):
            return sum(grid)

        m, n = len(grid), len(grid[0])


        dp = [[float('inf')]*(n+1) for _ in range(m+1)]

        dp[0][1] = 0

        for i in range(1, m+1):
            for j in range(1,n+1):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i-1][j-1]

        return dp[-1][-1]

    def minPathSum(self, grid):
        '''
        dp[i][j] 代表 （0,0）->（i-1.j-1） 最短路径

        dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i-1][j-1]

        dp[0][j] = inf
        dp[i][0] = inf
        dp[0][1] = 0

        res = dp[-1][-1]

        空间优化 O(n)
        '''
        if not grid:
            return -1

        if grid and not isinstance(grid[0], list):
            return sum(grid)

        m, n = len(grid), len(grid[0])


        dp = [float('inf')]*(n+1)

        dp[1] = 0

        for i in range(1, m+1):
            for j in range(1,n+1):
                dp[j] = min(dp[j-1], dp[j]) + grid[i-1][j-1]

        return dp[-1]