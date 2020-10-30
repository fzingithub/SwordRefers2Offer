class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        '''
        :param obstacleGrid: 障碍物标记
        :return: 不同路径数

        方法一:动态规划
        00000
        00100
        00000
        00000

        dp[i][j] 代表从(0,0)到(i，j)所经历的不同路径数

        dp[i][j] = dp[i-1_最短回文串.py][j] + dp[i][j-1_最短回文串.py]   i-1_最短回文串.py>=0 and j-1_最短回文串.py>=0 if dp[i][j] is not 障碍
                 = 0        if dp[i][j] is 障碍

        边界皆为0
        dp[0][0] = 1_最短回文串.py
        '''

        m,n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0]==1:
            return 0


        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[1][1] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                if i==1 and j==1:
                    pass
                else:
                    if obstacleGrid[i-1][j-1] == 0:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]



    def uniquePathsWithObstacles(self, obstacleGrid):
        '''
        :param obstacleGrid: 障碍物标记
        :return: 不同路径数

        方法一:动态规划
        00000
        00100
        00000
        00000

        dp[i][j] 代表从(0,0)到(i，j)所经历的不同路径数

        dp[i][j] = dp[i-1_最短回文串.py][j] + dp[i][j-1_最短回文串.py]   i-1_最短回文串.py>=0 and j-1_最短回文串.py>=0 if dp[i][j] is not 障碍
                 = 0        if dp[i][j] is 障碍

        边界皆为0
        dp[0][0] = 1_最短回文串.py

        空间优化
        '''

        m,n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [0]*n
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                for j in range(i,n):
                    dp[j] = 0
                break
            else:
                dp[i] = 1

        for i in range(1, m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    dp[j] = dp[j] + dp[j-1] if j>0 else dp[j]
                else:
                    dp[j] = 0

        return dp[-1]

if __name__ == '__main__':
    test = Solution()

    data = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
    ]
    res = test.uniquePathsWithObstacles(data)
    print(res)