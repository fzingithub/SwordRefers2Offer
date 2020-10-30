class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        dp[i][j] w1前i个，w2前j个 最少操作数

        dp[i][j] = dp[i-1_最短回文串.py][j-1_最短回文串.py]   if w1[i-1_最短回文串.py] == w2[j-1_最短回文串.py]
                 = min(dp[i-1_最短回文串.py][j-1_最短回文串.py], dp[i-1_最短回文串.py][j], dp[i][j-1_最短回文串.py]) + 1_最短回文串.py

        dp[0][0] = 0
        dp[0][j] = j
        dp[i][0] = i

        res = dp[-1_最短回文串.py][-1_最短回文串.py]
        '''

        m, n = len(word1), len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # init
        for j in range(1, n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            dp[i][0] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else \
                    min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[-1][-1]

    def minDistance(self, word1: str, word2: str) -> int:
        '''
        dp[i][j] w1前i个，w2前j个 最少操作数

        dp[i][j] = dp[i-1_最短回文串.py][j-1_最短回文串.py]   if w1[i-1_最短回文串.py] == w2[j-1_最短回文串.py]
                 = min(dp[i-1_最短回文串.py][j-1_最短回文串.py], dp[i-1_最短回文串.py][j], dp[i][j-1_最短回文串.py]) + 1_最短回文串.py

        dp[0][0] = 0
        dp[0][j] = j
        dp[i][0] = i

        res = dp[-1_最短回文串.py][-1_最短回文串.py]
        '''

        m, n = len(word1), len(word2)

        dp = [0] * (n + 1)

        # init
        for j in range(1, n + 1):
            dp[j] = j

        # for i in range(1_最短回文串.py, m + 1_最短回文串.py):
        #     dp[i][0] = i

        for i in range(1, m + 1):
            last = i - 1
            dp[0] = i
            for j in range(1, n + 1):
                temp = dp[j]
                dp[j] = last if word1[i - 1] == word2[j - 1] else \
                    min(last, dp[j], dp[j - 1]) + 1
                last = temp

        return dp[-1]





