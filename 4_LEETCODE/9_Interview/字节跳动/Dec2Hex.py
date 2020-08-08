class Solution:
    def D2H(self, num):
        '''
        十进制转十六进制
        负数 32bit 补 正
        '''

        num = num + 2**32 if num < 0 else num

        res = []
        while num:
            low = num % 16
            num = num // 16
            res.append(low)

        res = res[::-1]

        mapList = ['a', 'b', 'c', 'd', 'e', 'f']

        for i in range(len(res)):
            if res[i] > 9:
                res[i] = mapList[res[i]-10]
        return ''.join(map(str, res))

if __name__ == '__main__':
    test = Solution()

    res = test.D2H(-1)
    print(res)