class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        先找出t中第一个s[0]出现的位置idx
        t=t[idx:]

        dp[i][j] 表示s前i个字符和t前j个字符是否匹配
        abc   ajhbdbc
        dp[i][j] =dp[i-1_最短回文串.py][j-1_最短回文串.py] or dp[i][j-1_最短回文串.py]  if s[i-1_最短回文串.py]==t[j-1_最短回文串.py]
                 =dp[i][j-1_最短回文串.py]

        dp[0][j] = False
        dp[i][0] = False
        dp[0][0] = True

        res = dp[-1_最短回文串.py][-1_最短回文串.py]
        '''
        if not s:
            return True

        idx = t.find(s[0])
        t = t[idx:]

        m, n = len(s), len(t)

        dp = [[False]*(n+1) for _ in range(m+1)]

        dp[0][0] = True

        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i - 1][j - 1] or dp[i][j - 1] if s[i - 1] == t[j - 1] else dp[i][j - 1]

        return dp[-1][-1]

    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        双指针+贪心：假定当前需要匹配字符 c，而字符 c 在 t 中的位置 x_1和 x_2出现（x_1<x_2），那么贪心取 x_1是最优解，因为 x_2后面能取到的字符，x_1也都能取到，并且通过 x_1与 x_2之间的可选字符，更有希望能匹配成功。这样，我们初始化两个指针 ii 和 jj，分别指向 ss 和 tt 的初始位置。每次贪心地匹配，匹配成功则 ii 和 jj 同时右移，匹配 ss 的下一个位置，匹配失败则 jj 右移，ii 不变，尝试用 tt 的下一个字符匹配 ss。
        最终如果 i 移动到 s 的末尾，就说明 s 是 t 的子序列。
        '''

        i, j = 0, 0
        m, n = len(s), len(t)

        while i<m and j<n:
            if s[i]==t[j]:
                i += 1
                j += 1
            else:
                j += 1

        return i>=m


if __name__ == '__main__':
    test = Solution()
    s, t = 'abc', 'vcaddfsdfdffbdbc'
    res = test.isSubsequence(s, t)

    print(res)
