class Solution:
    def fib(self, n):
        '''
        分析：
        dp[i] = dp[i-1]+dp[i-2]
        '''

        n0 = 0
        n1 = 1
        if n==0:
            return 0

        for i in range(2,n+1):
            last = n1
            n1 = n0+n1
            n0 = last

        return n1
