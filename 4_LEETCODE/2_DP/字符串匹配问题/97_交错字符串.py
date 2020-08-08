class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        dp[i][j] 代表 前i个s1,与前j个s2,是否交错组成前i+j个s3

        dp[0][0] = True
        dp[0][j]
        dp[j][0]

        dp[i][j] = dp[i-1][j] if s1[i-1] == s3[i+j-1]
                 = dp[i][j-1] if s2[j-1] == s3[i+j-1]
                 = dp[i-1][j] or dp[i][j-1] if s2[j-1] == s1[i-1] == s3[i+j-1]


        res = dp[-1][-1]
        '''

        m, n, s = len(s1), len(s2), len(s3)

        if s != m + n:
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # init
        dp[0][0] = True
        for i in range(1, n + 1):
            # s2
            if s2[i - 1] == s3[i - 1]:
                dp[0][i] = dp[0][i - 1]

        for i in range(1, m + 1):
            # s1
            if s1[i - 1] == s3[i - 1]:
                dp[i][0] = dp[i - 1][0]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j - 1]
                elif s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = False

        return dp[-1][-1]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        dp[i][j] 代表 前i个s1,与前j个s2,是否交错组成前i+j个s3

        dp[0][0] = True
        dp[0][j]
        dp[j][0]

        dp[i][j] = dp[i-1][j] if s1[i-1] == s3[i+j-1]
                 = dp[i][j-1] if s2[j-1] == s3[i+j-1]
                 = dp[i-1][j] or dp[i][j-1] if s2[j-1] == s1[i-1] == s3[i+j-1]


        res = dp[-1][-1]
        '''

        m, n, s = len(s1), len(s2), len(s3)

        if s != m + n:
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # init
        dp[0][0] = True
        for i in range(1, n + 1):
            # s2
            if s2[i - 1] == s3[i - 1]:
                dp[0][i] = dp[0][i - 1]

        for i in range(1, m + 1):
            # s1
            if s1[i - 1] == s3[i - 1]:
                dp[i][0] = dp[i - 1][0]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i][j - 1]
                elif s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = False

        return dp[-1][-1]

if __name__ == '__main__':
    test = Solution()

    s1, s2, s3 = "aabcc", "dbbca", "aadbbcbcac"

    res = test.isInterleave(s1, s2, s3)

    print(res)