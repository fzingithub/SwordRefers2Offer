class Solution:
    def singleNumber(self, nums):
        '''
        位运算：统计二进制各个位置上出现的次数，取余3即为答案
        方法一：有限状态自动机，进位 *
        方法二：统计
        '''
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones

    def singleNumber1(self, nums):
        '''
        位运算：统计二进制各个位置上出现的次数，取余3即为答案
        方法一：有限状态自动机，进位
        方法二：统计 *
        '''
        numBit = [0]*32

        for i in nums:
            num = i
            index = 0
            while num:
                if num&1:
                    numBit[index]+=1
                num = num>>1
                index += 1

        for i in range(32):
            numBit[i] = numBit[i]%3

        res = 0
        base = 1
        for i in range(32):
            if numBit[i]:
                res += base
            base *= 2

        return res

if __name__ == '__main__':
    test = Solution()
    res = test.singleNumber([3,4,3,4,3,5,4])

    print(res)


