class Solution:
    def maxProdcutSplit(self, s:int, m:int):
        '''
        拆分 s 使其积大于等于 m 的最小拆分次数
        方法一： 纯贪心+二分+快速幂
        '''
        times = s // 3 # 贪心求出最多分的次数
        remainder = s % 3

        if remainder==1 or remainder==0:
            times -= 1  # 若余数为1最多分 times-1 次

        def biSearch(left, right):
            while left<right:
                mid = left + (right - left) // 2  # 分 mid 次

                base = s // (mid + 1)
                remain = s % (mid + 1)
                product = pow(base, mid + 1) if remain == 0 else pow(base, mid) * (base + remain)

                if product>=m:
                    right = mid
                else:
                    left = mid+1

            return left

        return biSearch(0, times)




if __name__ == '__main__':
    test = Solution()

    res = test.maxProdcutSplit(333, 43434)

    print(res)