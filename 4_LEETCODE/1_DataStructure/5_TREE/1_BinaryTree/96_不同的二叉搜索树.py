class Soluiton:
    def numTrees(self, n):
        '''
        方法一： 动态规划

        G[n] 代表 以 1 ... n 为节点组成的二叉搜索树有多少种, 前n个数。
        F[i][n] 以i为根，以 1 ... n 为节点组成的二叉搜索树有多少种 i<=n
        G[0] = 1
        G[1] = 1

        G[n] = \sum_{i=0}^{n}F[i][n]

        1,2,3,4,5,...,j,...,n

        G[n] = \sum_{j = 1}^{n} G[j-1]*G[n-j]

        res = G[n]
        T:O(n^2)
        M:O(n)
        '''

        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[-1]

    def numTrees(self, n):
        '''
        方法二： 卡塔兰数
        G[n] = \sum_{j = 1}^{n} G[j-1]*G[n-j]       索引值相加为 n-1
        通项公式：
        G[n+1] = \frac{2(2n+1)}{n+2} G[n]
        G[0] = 1

        T:O(n)
        M:O(1)
        '''
        last = 1

        for i in range(0, n):
            last =last*2*(2*i+1)//(i+2)

        return last

# C语言版
# int numTrees(int n){
#     long long  last = 1;
#
#     for (int i = 0;i<n;++i){
#         last = last*2*(2*i+1)/(i+2);
#     }
#     return (int)last;
#
# }