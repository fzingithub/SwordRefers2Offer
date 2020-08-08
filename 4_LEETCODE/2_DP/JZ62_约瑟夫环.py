class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        '''
        dp[i][j]

        dp[10][5]   0,1,2,3,4,5,6,7,8,9,10

        dp[9][5]    0,1,2,3,4,5,6,7,8,9
                    5,6,7,8,9,10,0,1,2,3

        dp[10][5] = (dp[9][5] + 5) % 10

        dp[i][m] = (dp[i-1][m] + m) % i

        '''
        last = 0
        for i in range(2, n + 1):
            last = (last + m) % i

        return last