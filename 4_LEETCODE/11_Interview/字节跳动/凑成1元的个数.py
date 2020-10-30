class Solution:
    def numOfsum1(self, n):
        '''
        n 分钱
        1_最短回文串.py 2 5 分硬币不限，凑成1元有多少种方法.

        暴力 O(n^3)
        '''
        res = 0
        for i in range(n+1):
            for j in range(n//2+1):
                for k in range(n//5+1):
                    if i + j*2 + k*5 == n:
                        res += 1

        return res

    def numOfsum1_dp(self, n):
        '''
        n 元钱
        1_最短回文串.py 2 5 分硬币不限，凑成100分有多少种方法.
        w[3] = [1_最短回文串.py, 2, 5]
        动态规划
        dp[i][j] 把第一个硬币凑成j分钱一共有多少种方法。

        sum = n1*1_最短回文串.py+n2*2+n5*5
        dp[i][j] = dp[i-1_最短回文串.py][j] + dp[i-1_最短回文串.py][j-w[i]] + ... + dp[i-1_最短回文串.py][j-kw[i]]

        边界
        dp[0][j] = 0
        dp[i][0] = 1_最短回文串.py    i= 0, 1_最短回文串.py, ...
        '''
        w = [1,2,5]
        m = 3
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = 1

        for i in range(1,m+1):
            for j in range(w[i-1],n+1):
                for k in range(0, j//w[i-1]+1):
                    dp[i][j] += dp[i-1][j-k*w[i-1]]

        return dp[-1][-1]

    def numOfsum1_dp(self, n):
        '''
        n 元钱
        1_最短回文串.py 2 5 分硬币不限，凑成100分有多少种方法.
        w[3] = [1_最短回文串.py, 2, 5]
        动态规划
        dp[i][j] 把第一个硬币凑成j分钱一共有多少种方法。

        sum = n1*1_最短回文串.py+n2*2+n5*5
        dp[i][j] = dp[i-1_最短回文串.py][j] + dp[i-1_最短回文串.py][j-w[i]] + ... + dp[i-1_最短回文串.py][j-kw[i]]

        边界
        dp[0][j] = 0
        dp[i][0] = 1_最短回文串.py    i= 0, 1_最短回文串.py, ...

        空间时间极致优化 O(mn)  空间：O(n)
        '''
        w = [1, 5, 2]
        m = 3
        dp = [0] * (n + 1)
        dp[0] = 1



        for i in range(1, m + 1):
            for j in range(w[i - 1], n+1):
                    dp[j] += dp[j - w[i - 1]]

        return dp[-1]



if __name__ == '__main__':
    test = Solution()
    res = test.numOfsum1(100)
    print(res)
