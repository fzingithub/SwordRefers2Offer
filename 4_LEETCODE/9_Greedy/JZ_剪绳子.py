class Solution:
    def cuttingRope(self, n):
        '''
        动态规划：
        dp[j] 长度为j的最大积；

        dp[j] = max(dp[i]*dp[j-i]) i = 0, 1, ... ,j//2.

        边界 dp[0] = 0
            dp[1] = 1
            dp[2] = 2
            dp[3] = 3

        res = dp[-1]

        时间 O(n^2)
        空间 O(n)
        '''

        dp = [0, 1, 2, 3]

        res = [0, 1, 1, 2]
        if n<4:
            return res[n]
        res = 0

        for i in range(4, n+1):
            temp = 0
            for j in range(1, i//2+1):
                temp = max(temp, dp[j]*dp[i-j])
            dp.append(temp)

        return dp[-1]

    def cuttingRope(self, n):
        '''
        贪心算法：
        i = 1， 2， 3 时不减最大
        所以尽量多减 3
        当有1 的时候 减个2 2

        时间 O(1)
        空间 O(1)
        '''
        res = [0, 1, 1, 2]
        if n<4:
            return res[n]

        if n%3 == 1:
            num3 = (n-4) // 3
            return 3**num3 * 4
        elif n%3 == 2:
            num3 = n//3
            return 3 ** num3 * 2
        else:
            num3 = n // 3
            return 3 ** num3








if __name__ == '__main__':
    test= Solution()

    res = test.cuttingRope(1000) % 100000007

    print(res)
