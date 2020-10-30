class Solution:
    def numWays(self, n):
        '''
        分析：
        dp[i] = dp[i-1_最短回文串.py]+dp[i-2]
        边界 dp[0] = 1_最短回文串.py
            dp[1_最短回文串.py] = 1_最短回文串.py
        '''

        n0 = 1
        n1 = 1

        for _ in range(1,n):
            n1, n0 = n0+n1, n1

        return n1%1000000007