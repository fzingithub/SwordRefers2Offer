class Solution:
    # 动态规划 时间复杂度O(n^2) 空间复杂度O(m*n)
    # dp[i][j] A[0...i] B[0...j] 的最大公共子序列
    # dp[i+1][j+1] = dp[i][j] + 1 if A[i+1] == B[j+1]
    #              = max(dp[i][j+1], dp[i+1][j])
    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:

        if not text1 or not text2:
            return 0

        length1 = len(text1)
        length2 = len(text2)

        dp = [[0] * (length2 + 1) for _ in range(length1 + 1)]

        for i in range(length1):
            for j in range(length2):
                dp[i + 1][j + 1] = dp[i][j] + 1 if text1[i] == text2[j] else max(dp[i + 1][j], dp[i][j + 1])

        return dp[-1][-1]

    # 动态规划空间优化 时间复杂度O(n^2) 空间复杂度O(min(m,n))
    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:

        if not text1 or not text2:
            return 0

        length1 = len(text1)
        length2 = len(text2)

        dp = [0] * (length2 + 1)

        for i in range(length1):
            temp = dp[:]
            for j in range(length2):
                dp[j + 1] = temp[j] + 1 if text1[i] == text2[j] else max(dp[j], temp[j + 1])

        return dp[-1]

    # 动态规划空间再优化
    def longestCommonSubsequence3(self, text1, text2):

        if not text1 or not text2:
            return 0

        length1 = len(text1)
        length2 = len(text2)

        dp = [0] * (length2 + 1)

        for i in range(length1):
            last_j = 0
            for j in range(length2):
                temp = dp[j+1]
                dp[j + 1] = last_j + 1 if text1[i] == text2[j] else max(dp[j], dp[j + 1])
                last_j = temp
        return dp[-1]