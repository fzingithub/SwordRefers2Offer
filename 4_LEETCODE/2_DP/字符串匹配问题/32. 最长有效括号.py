class Solution:
    def longestvalid(self, s):
        '''
        方法一： 暴力，最长一定是偶数，从大到小用栈判定 时间 O(n^3) 空间 O(1_最短回文串.py)
        :param s:  只包含 '(', ')'的串
        :return: 最长有效子串长度
        '''
        def isValid(s):
            stack = []
            for k in range(len(s)):
                if s[k] == ')':
                    if stack and stack[0] == '(':
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(s[k])
            if not stack:
                return True
            else:
                return False


        if not s:
            return 0

        length = len(s)
        longestEven = length if length%2==0 else length-1

        for i in range(longestEven,0,-2): # 有效长度 从大到小 必为偶数
            for j in range(0, length-i+1): # 起始点
                if isValid(s[j:j+i]):
                    return i

        return 0

    def longestvalid2(self, s):
        '''
        方法二： 动态规划
        dp[i] 以下标i结尾的最长有效子串长度
        dp[i+1_最短回文串.py] = dp[i-dp[i]-2]+2+dp[i]  i-dp[i]-1_最短回文串.py>=0
        i-dp[i]-2 有可能是 -1_最短回文串.py 也满足情况 初始化 dp[-1_最短回文串.py] = 0

        时间复杂度 O(n)
        空间复杂度 O(n)
        :param s:  只包含 '(', ')'的串
        :return: 最长有效子串长度
        '''
        if not s:
            return 0

        length = len(s)
        dp = [0] *length

        for i in range(length):
            if s[i] == ')' and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1] == '(':
                dp[i] = 2+dp[i-1]+dp[i-dp[i-1]-2]

        return max(dp)

    def longestvalid3(self, s):
        '''
        方法三： 栈模拟
        当 遇到 ")" 栈顶元素出栈 栈不为空 表示一定匹配到 就更新 res 的值
        此时栈顶元素就是合法串的前一个字符索引 默认-1_最短回文串.py
        :param s:  只包含 '(', ')'的串
        :return: 最长有效子串长度
        '''
        if not s:
            return 0

        stack = [-1]
        length = len(s)
        res = 0
        for i in range(length):
            if s[i] == ')':
                stack.pop()
                if not stack:
                    stack.append(i)
                else: # 栈不为空 表示一定匹配到 就更新 res 的值 此时栈顶元素就是合法串的前一个字符索引
                    res = max(res, i-stack[-1])
            else:
                stack.append(i)

        return res

    def longestvalid(self, s):
        '''
        方法三： 左右遍历记录两字符的个数 相等时更新 right>left 时重置
        :param s:  只包含 '(', ')'的串
        :return: 最长有效子串长度
        '''
        if not s:
            return 0

        leftNum = 0
        rightNum = 0
        res = 0

        for i in s:
            if i == '(':
                leftNum += 1
            else:
                rightNum += 1

            if rightNum > leftNum:
                leftNum = 0
                rightNum = 0
            elif rightNum == leftNum:
                res = max(res, leftNum*2)

        leftNum = 0
        rightNum = 0
        for i in s[::-1]:
            if i == '(':
                leftNum += 1
            else:
                rightNum += 1

            if leftNum > rightNum:
                leftNum = 0
                rightNum = 0
            elif rightNum == leftNum:
                res = max(res, leftNum*2)

        return res

if __name__ == '__main__':
    test = Solution()
    s = "())"
    # print(len(s))
    res = test.longestvalid(s)
    print(res)





