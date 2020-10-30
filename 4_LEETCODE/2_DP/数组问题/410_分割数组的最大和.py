class Soluition:
    def splitArray(self, nums, m):
        '''
        动态规划
        dp[i][j] 前i个数 分j次 和最大值最小
        [7,2,5,10,8]   m=5
      0 [0,inf,inf,inf,inf,inf]
         inf,7,inf,inf,inf,inf
         inf,9,7,inf,inf,inf
         inf,14,7,2,inf,inf
         inf,24,14,10,inf
         inf,32,18,

        dp[i][j] =  min(max(dp[k][j-1_最短回文串.py], sub_sum(k+1_最短回文串.py,i)), dp[i][j])    k<i      if j<=min(i,m)

        dp[i][0] = inf
        dp[0][j] = inf
        dp[0][0] = 0
        res = dp[-1_最短回文串.py][-1_最短回文串.py]
        '''
        m, n = len(nums), m

        dp = [[float('inf')]*(n+1) for _ in range(m+1)]
        dp[0][0] = 0

        subSum = [0]
        for i in nums:
            subSum.append(subSum[-1]+i)

        for i in range(1, m+1):
            for j in range(1, min(i,n)+1):
                for k in range(i):
                    dp[i][j] = min(max(dp[k][j - 1], subSum[i]-subSum[k]), dp[i][j])

        return dp[-1][-1]

    def splitArray(self, nums, m):
        '''
        二分+贪心
        当我们选定一个值 x，我们可以线性地验证是否存在一种分割方案，满足其最大分割子数组和不超过 x。策略如下：
            贪心地模拟分割的过程，从前到后遍历数组，用 sum 表示当前分割子数组的和，cnt 表示已经分割出的子数组的数量（包括当前子数组），
            那么每当 sum 加上当前值超过了 x，我们就把当前取的值作为新的一段分割子数组的开头，并将 cnt 加 1_最短回文串.py。
            遍历结束后验证是否 cnt 不超过 m。

        这样我们可以用二分查找来解决。二分的上界为数组 nums 中所有元素的和，下界为数组 nums 中所有元素的最大值。通过二分查找，
        我们可以得到最小的最大分割子数组和，这样就可以得到最终的答案了。
        '''

        def check(x: int) -> bool:
            total, cnt = 0, 1
            for num in nums:
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= m

        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == '__main__':
    test = Soluition()
    nums = [7, 2, 5, 10, 8]
    m = 2
    res = test.splitArray(nums, m)

    print(res)
