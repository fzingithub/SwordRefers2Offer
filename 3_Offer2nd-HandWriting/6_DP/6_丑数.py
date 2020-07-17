class Solution:
    def nthUglyNumber(self, n):
        '''
        1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。

        dp[n] 代表 第 n个丑数
        dp[n] = min(dp[p2]*2, dp[p3]*3, dp[p5]*5)
        p2为 乘2 大于 dp[-1] 的最小值索引
        p3为 乘3 大于 dp[-1] 的最小值索引
        p5为 乘5 大于 dp[-1] 的最小值索引
        易知： p2, p3, p4 不回溯

        边界 dp[0] = 1
        res = dp[-1]
        '''
        dp = [1]
        p2, p3, p5 = 0, 0, 0

        for i in range(1, n):
            Value = min(dp[p2]*2, dp[p3]*3, dp[p5]*5)
            dp.append(Value)


            while dp[p2]*2<=Value:
                p2 += 1
            while dp[p3]*3<=Value:
                p3 += 1
            while dp[p5]*5<=Value:
                p5 += 1

        return dp[-1]



    def nthUglyNumber(self, n):
        '''
        1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。

        dp[n] 代表 第 n个丑数
        dp[n] = min(dp[p2]*2, dp[p3]*3, dp[p5]*5)
        p2为 乘2 大于 dp[-1] 的最小值索引
        p3为 乘3 大于 dp[-1] 的最小值索引
        p5为 乘5 大于 dp[-1] 的最小值索引
        易知： p2, p3, p4 不回溯 并且 p2 p3 p5 最多 向右走一步

        边界 dp[0] = 1
        res = dp[-1]

        优化指针
        '''
        dp = [1]
        p2, p3, p5 = 0, 0, 0

        for i in range(1, n):
            value2, value3, value5 = dp[p2]*2, dp[p3]*3, dp[p5]*5
            value = min(value2, value3, value5)
            dp.append(value)


            if value == value2:
                p2 += 1
            if value == value3:
                p3 += 1
            if value == value5:
                p5 += 1

        return dp[-1]



