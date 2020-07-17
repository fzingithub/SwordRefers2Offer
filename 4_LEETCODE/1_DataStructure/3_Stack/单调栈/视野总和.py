class Solution:
    def viewSum(self, data):
        stack = [] #单调递增栈
        res = 0
        data.append(10**9) # 入栈最后一个元素设置为无限大 用于出栈


        for i in range(len(data)):
            if not stack or data[stack[-1]] > data[i]:
                stack.append(i)
            else:
                while stack and data[stack[-1]] <= data[i]:
                    top = stack.pop()
                    res += i - top -1

                stack.append(i)

        return res

if __name__ == '__main__':
    test = Solution()
    res = test.viewSum([8,4,3,4,2,1,7,1])
    print(res)

