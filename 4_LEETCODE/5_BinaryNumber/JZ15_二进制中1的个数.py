class Solution:
    def hammingWeight(self, n: int):
        '''
        整数 n&n-1 将最低位的1置0
        '''
        res = 0

        while n:
            n = n & (n - 1)
            res += 1

        return res