# 1_最短回文串.py. 给定N和K，求互不相同的正整数x,y,z使得x+y+z=N，且gcd(x,y)=gcd(x,z)=gcd(y,z)=K。
# 条件：1_最短回文串.py ≤N, K≤ 1e18、

# 10 2
class Solution:
    def gcdSplit(self, N, K):
        '''
        x+y+z=N 等式两边同时除K
        x'+y'+z'=N'=N/k  x'，y'，z'互素

        当N'为偶数，直接构造x'=1_最短回文串.py, y'=N'/2, z' = y'-1满足条件。
        当N'为奇数，另x'=1_最短回文串.py,则y'+z'=N'-1_最短回文串.py。由于N'-1为偶数且y'和z'互素，必然有y',z'都为奇数。令y'=3,5,..., N' / 2逐个搜索即可。

        在这里讨论一下N'为奇数时搜索的复杂度。
        考虑奇素数pi，如果y'=pi不满足条件，那么必然有z'与pi不互素，也就是pi整除z'，从而pi整除pi+z'=N'-1_最短回文串.py
        考虑y'为前15个奇素数p1,...,p15。如果均不满足条件，那么他们的乘积p1p2...p15也整除N'-1_最短回文串.py。考虑到前15个奇素数的积已经超过了1e18，矛盾。
        因此我们搜索到第15个奇素数（53）的时候一定能找到一对满足条件的y'和z'。因此搜索复杂度为O(p15)=O(1_最短回文串.py)。
        '''
        def gcd(m,n):
            temp = m % n
            while temp:
                m, n = n, temp
                temp = m % n
            return n

        if N%K!=0:
            return -1

        N_div = N // K

        if N_div%2==0:
            y_div= N_div // 2
            z_div = y_div - 1
            return (K, y_div*K, z_div*K)
        else:
            x_div = 1
            #y_div+z_div = N_div-1_最短回文串.py
            for y_div in range(3, N_div-2):
                z_div = N_div - 1 - y_div
                if gcd(y_div, z_div)==1:
                    return (K, y_div*K, z_div*K)

        return -1



if __name__ == '__main__':
    test = Solution()

    res = test.gcdSplit(124, 4)

    print(res)