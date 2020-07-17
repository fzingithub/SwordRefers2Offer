class Solution:
    # 暴力 时间 O(n^3) 空间O(1)
    def findLength(self, A, B):
        if not A or not B:
            return 0


        LengthA = len(A)
        LengthB = len(B)

        res = 0
        for i in range(LengthA):
            for j in range(LengthB):
                if A[i] == B[j]:
                    indexA = i
                    indexB = j
                    while indexA<LengthA and indexB<LengthB and A[indexA] == B[indexB]:
                        indexA += 1
                        indexB += 1
                    res = max(res, indexB-j)


        return res

    # 动态规划  时间复杂度O(n^2) 空间复杂度O(n*m)
    # dp[i][j] A[i]与B[j] 结尾的最大公共子串的长度
    # dp[i][j] = dp[i-1][j-1] + 1 if A[i] == B[j] 0
    # res = max(map(max, dp))
    def findLength2(self, A, B):
        if not A or not B:
            return 0

        lengthA = len(A)
        lengthB = len(B)

        dp = [[0] * (len(B)+1) for i in range(len(A)+1)]

        for i in range(lengthA):
            for j in range(lengthB):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1

        return max(map(max, dp))

    # 动态规划 空间优化 时间复杂度 O(n^2) 空间复杂度O(min(n,m))
    def findLength3(self, A, B):
        if not A or not B:
            return 0

        lengthA = len(A)
        lengthB = len(B)

        dp = [0] * (len(B)+1)
        res = 0
        for i in range(lengthA):
            for j in range(lengthB-1, -1, -1):
                dp[j+1] = dp[j] + 1 if A[i] == B[j] else 0
            res = max(res, max(dp))

        return res


if __name__ == '__main__':
    test = Solution()

    res = test.findLength3(
        [1, 0, 0, 0, 1],
        [1, 0, 0, 1, 1]
    )
    print(res)