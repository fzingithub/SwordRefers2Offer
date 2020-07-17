class Solution:
    def isMatch(self, s, p):
        '''
        dp[i][j] 代表s[:i] p[:j]是否匹配

        dp[i][j] = dp[i-1][j-1]  if s[i] == p[j] or p[j] == '.'  match
                 = dp[i][j-2]              不匹配                                p[j] == '*'
                 = dp[i-1][j-2]            匹配一个字符      s[i]=p[j−1]          p[j] == '*'
                 = dp[i-2][j-2]            匹配两个字符     s[i−1]=s[i]=p[j−1]     p[j] == '*'
                 ...

                 核心重点：字母 * 星号的组合在匹配的过程中，本质上只会有两种情况：
                 1. 匹配 s 末尾的一个字符，将该字符扔掉，而该组合还可以继续进行匹配；
                 2. 不匹配字符，将该组合扔掉，不再进行匹配。

        dp[i][j] = dp[i-1][j-1]  if s[i] == p[j] or p[j] == '.'  令为 match(i, j)
                 = dp[i-1][j] or dp[i][j-2]   if p[j] == '*' and match(i, j-1)
                 = dp[i][j-2]                 if p[j] == '*' and not match(i, j-1)

        边界：  dp[0][0] True
                dp[i][0] False
                dp[0][j] 分情况讨论了， 连续偶数个 * True p = 'a*.*'
        '''
        def match(i, j):
            '''
            :param i:  s 的索引
            :param j:  p 的索引
            :return: 是否单个匹配
            '''
            if j<0 :
                return False
            if s[i]==p[j] or p[j]=='.':
                return True
            else:
                return False



        m, n = len(s), len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]

        # 限定边界
        dp[0][0] = True

        for j in range(1, n, 2):
            if p[j] == '*':
                dp[0][j+1] = True
            else:
                break

        # 状态转移
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    if match(i-1, j-2):
                        dp[i][j] = dp[i-1][j] or dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j-2]
                else:
                    if match(i-1, j-1):
                        dp[i][j] = dp[i-1][j-1]

        return dp[-1][-1]

if __name__ == '__main__':
    test = Solution()

    res = test.isMatch('adkfffffle', 'ad.f*fle')
    print(res)

