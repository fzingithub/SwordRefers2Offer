class Solution:
    def maxProfit1(self, prices):
        '''
        [7,1_最短回文串.py,5,3,6,4]

        dp[i] = prices[i] - buy if price[i]>buy
                0, buy = prices[i]

        边界 buy = 无穷大
        res = max(dp)

        时间 空间优化
        '''
        m = len(prices)



        buy = float('inf')
        res = 0
        for i in range(m):
            if prices[i] > buy:
                res = max(res, prices[i] - buy)
            else:
                buy = prices[i]
        return res

    def maxProfit(self, prices):
        '''
        单调栈：
        [7,1_最短回文串.py,5,3,6,4]

        stack = [1_最短回文串.py,2,3]  #单调递减栈
        出栈产生利润
        '''
        stack = []

        res = 0

        for i in prices:
            flag = 0
            while stack and stack[-1]>i:
                if flag == 0:
                    res = max(res, stack[-1]-stack[0])
                    flag = 1
                stack.pop()

            stack.append(i)

        if stack:
            res = max(res, stack[-1]-stack[0])

        return res


if __name__ == '__main__':
    test = Solution()

    res = test.maxProfit([7,1,5,3,6,4])

    print(res)