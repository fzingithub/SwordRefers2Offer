class Solution:
    def isMatch(self, s, p):
        '''
        方法一： 动态规划
        dp[i][j] 代表 子串s[:i] 与子模式p[:j] 是否匹配
        dp[i][j] = dp[i-1][j-1]   if s[i]==p[j] or p[j] == '?'
                 = dp[i][j−1] or dp[i−1][j]  if p[j] = '*'
                 = False   otherwise
        边界： dp[0][0]=True，即当字符串 s 和模式 p 均为空时，匹配成功；
              dp[i][0]=False，即空模式无法匹配非空字符串；
              dp[0][j] 需要分情况讨论：因为星号才能匹配空字符串，所以只有当模式 p的前 j个字符均为星号时，dp[0][j]才为真。

        :param s: 字符串
        :param p: 串模式
        :return: True or False
        '''

        m, n = len(s), len(p)

        # 初始化
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True

        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = True
            else:
                break

        # 状态转移
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif p[j-1] == s[i-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = False
        return dp[-1][-1]

if __name__ == '__main__':
    test = Solution()

    res = test.isMatch('aa', '*')

    print(res)




