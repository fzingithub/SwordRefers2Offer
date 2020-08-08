class Solution:
    def integerBreak(self, n:int)->int:
        '''
        dp[i] 代表整数i的最大积拆分

        dp[i] = max(dp[i-j] * dp[j]) j=1,...,i-1.

        dp[0-3] = 0, 1, 2, 3

        res = dp[-1]
        '''

        dp = [0,1,2,3]
        if n<2:
            return -1
        elif n==2:
            return 1
        elif n==3:
            return 2

        for i in range(4, n+1):
            temp = 0
            for j in range(1, i//2+1):
                temp = max(temp, dp[j]*dp[i-j])
            dp.append(temp)

        return dp[n]



    def integerBreak(self, n:int)-> int:
        '''
        贪心： 多分3 尾为1分2，2
        '''
        if n < 2:
            return -1
        elif n == 2:
            return 1
        elif n == 3:
            return 2

        i,j = n//3, n%3

        if j==1:
            return 4 * 3 ** (i-1)
        elif j==2:
            return 2 * 3 ** i
        else:
            return 3 ** i

