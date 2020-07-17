class Solution:
    def maxSubArray(self, nums):
        '''
        [-2,1,-3,4,-1,2,1,-5,4]

        dp[i] 以i结尾子数组的最大和

        dp[i] = dp[i] + nums[i] if dp[i]+nums[i]>nums
              = nums[i]


        dp[0] = 0
        res = max(dp)
        '''
        m = len(nums)

        dp = [0] * (m+1)

        for i in range(1, m+1):
            dp[i] = max(nums[i-1], dp[i-1]+nums[i-1])

        return max(dp[1:])


    def maxSubArray(self, nums):
        '''
        [-2,1,-3,4,-1,2,1,-5,4]

        dp[i] 以i结尾子数组的最大和

        dp[i] = dp[i] + nums[i] if dp[i]+nums[i]>nums
              = nums[i]


        dp[0] = 0
        res = max(dp)

        空间优化
        '''
        m = len(nums)

        last = -float('inf')
        res = -float('inf')

        for i in range(1, m+1):
            last = max(nums[i-1], last+nums[i-1])
            res = max(res, last)

        return res


if __name__ == '__main__':
    test = Solution()
    data = [-1]
    res = test.maxSubArray(data)

    print(res)