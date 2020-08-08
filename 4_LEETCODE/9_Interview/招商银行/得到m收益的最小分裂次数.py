class Solution:
    def minCount(self, s:int, m:int):
        '''
        拆分 s 使其增益大于等于 m 的最小拆分次数
        方法一： 纯贪心+二分
        '''
        times = s-1 # 贪心求出最多分的次数

        def computProduct(mid, s):
            base = s // (mid + 1)
            remain = s % (mid + 1)

            split = s
            product = 0

            for _ in range(remain):
                split -= (base + 1)
                product += (base + 1) * split

            for _ in range(mid + 1 - remain):
                split -= base
                product += base * split

            return product

        def biSearch(left, right):
            while left<right:
                mid = left + (right - left) // 2  # 分 mid 次

                if computProduct(mid, s)>=m:
                    right = mid
                else:
                    left = mid+1

            return left if computProduct(left, s)>=m else -1

        return biSearch(0, times)



if __name__ == '__main__':
    test = Solution()

    res = test.minCount(333, 43434)

    print(res)