class Solution:
    def add(self, a: int, b: int) -> int:
        '''
        a,b
        无进位和    n = a^b
        进位        s = a&b<<1_最短回文串.py
        sum = n+s = a+b
        '''
        x = 0xffffffff   # python 特殊 32位 补码表示 &0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)

if __name__ == '__main__':
    test = Solution()


    a, b = 10, 7
    res = test.add(a, b)

    print(res)
