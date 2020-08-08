class Solution:
    '''
    最大公约数
    greatest common divisor:     gcd(m,n) = k
    最小公倍数
    Least common multiple:      lcm(m,n) = m*n*k

    所以求最小公倍数 等于求最大公约数
    '''
    def gcd(self, m, n):
        '''
        辗转相除 对数级的时间复杂度
        '''
        if m<n:
            m,n = n,m
        while n:
            temp = m%n
            m,n = n,temp
        return m

    def gcd_(self, m, n):
        '''
        更相减损
        '''
        while m!=n:
            if m>n:
                m -= n
            elif m<n:
                n-= m

        return n



if __name__ == '__main__':
    test = Solution()
    res = test.gcd(8,12)
    print(res)

