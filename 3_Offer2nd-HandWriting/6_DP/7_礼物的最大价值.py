class Soluton:
    def maxValue(self, grid):
        '''
        dp[i][j] 从(0, 0)走到(i, j) 的最大价值
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        边界 dp[i][0] = 0 dp[0][i]

        res = dp[-1][-1]
        时间复杂度 O(mn)
        空间      O(mn)
        '''

        m, n = len(grid), len(grid[0])

        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1, n+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]

        return dp[-1][-1]

    def maxValue(self, grid):
        '''
        dp[i][j] 从(0, 0)走到(i, j) 的最大价值
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        边界 dp[i][0] = 0 dp[0][i] = 0

        res = dp[-1][-1]
        时间复杂度 O(mn)
        空间      O(n)

        空间优化
        '''

        m, n = len(grid), len(grid[0])

        dp = [0] * (n+1)

        for i in range(1,m+1):
            for j in range(1, n+1):
                dp[j] = max(dp[j], dp[j-1]) + grid[i-1][j-1]

        return dp[-1]


if __name__ == '__main__':
    test = Soluton()
    grid = [
        [1,3,1],
        [1,5,1],
        [4,2,1]
        ]
    res = test.maxValue(grid)

    print(res)
