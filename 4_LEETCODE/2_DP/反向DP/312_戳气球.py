class Solution:
    def maxCoins(self, nums):
        '''
        dp[i][j] 代表（i，j）最大硬币数

        dp[i][j] = max(dp[i][k] + dp[k][j]+ nums[i]*num[k]*nums[j]) i<k<j

        dp[i][j]=0  i>=j-1

        res = dp[0][n+1]

        '''
        n = len(nums)
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        nums = [1] + nums + [1]

        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][k] + dp[k][j]+ nums[i]*nums[k]*nums[j], dp[i][j])

        return dp[0][n + 1]

if __name__ == '__main__':
    test = Solution()

    res = test.maxCoins([3,1,5,8])

    print(res)