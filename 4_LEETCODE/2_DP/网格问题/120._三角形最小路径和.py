class Soluton:
    def  minimumTotal(self, triangle: list) -> int:
        '''
        dp

        dp[i][j] 从triangle[0][0] 到 triangle[i][j] 最小路径

        dp[i][j] = min(dp[i-1][j] + tri[i-1][j-1], dp[i-1][j-1] + tri[i-1][j-1])

        dp[0][j] = 'inf'
        dp[i][0] = 'inf'
        dp[0][0] = 0

        res = max(dp[-1])
        空间 O(m^2) 时间 O(m)
        '''
        m = len(triangle)

        dp = [[float('inf')] * (m+1) for _ in range(m+1)]
        dp[0][1] = 0

        for i in range(1, m+1):
            for j in range(1, i+1):
                dp[i][j] = min(dp[i-1][j] + triangle[i-1][j-1], dp[i-1][j-1] + triangle[i-1][j-1])
        return min(dp[-1])

    def  minimumTotal(self, triangle: list) -> int:
        '''
        dp

        dp[i][j] 从triangle[0][0] 到 triangle[i][j] 最小路径

        dp[i][j] = min(dp[i-1][j] + tri[i-1][j-1], dp[i-1][j-1] + tri[i-1][j-1])

        dp[0][j] = 'inf'
        dp[i][0] = 'inf'
        dp[0][0] = 0

        res = max(dp[-1])

        空间优化 O(m)
        '''
        m = len(triangle)

        dp = [float('inf')] * (m+1)
        dp[1] = 0

        for i in range(1, m+1):
            for j in range(i, 0, -1):
                dp[j] = min(dp[j] + triangle[i-1][j-1], dp[j-1] + triangle[i-1][j-1])
        return min(dp)

if __name__ == '__main__':
    test = Soluton()
    triangle = [
     [2],
    [3,4],
   [6,5,0],
  [4,1,8,3]
]
    res = test.minimumTotal(triangle)

    print(res)
