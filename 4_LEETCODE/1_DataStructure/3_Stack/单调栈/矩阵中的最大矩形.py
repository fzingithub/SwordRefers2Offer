class Solution:
    def largestRectangleArea(self, heights):
        if not heights:
            return 0

        length = len(heights)

        minL = [-1] * length
        minR = [-1] * length

        Stack = [] # 单调递减栈

        for i in range(length):
            while Stack and heights[i] <= heights[Stack[-1]]:
                Stack.pop()

            minL[i] = 0 if not Stack else Stack[-1] + 1
            Stack.append(i)

        Stack.clear()
        for i in range(length-1, -1, -1):
            while Stack and heights[i] <= heights[Stack[-1]]:
                Stack.pop()

            minR[i] = length-1 if not Stack else Stack[-1] - 1
            Stack.append(i)

        tempL = [-1] * length
        for i in range(length):
            tempL[i] = (minR[i] - minL[i] + 1) * heights[i]

        return max(tempL)

if __name__ == '__main__':
    test = Solution()
    res = test.largestRectangleArea([2,1,5,6,2,3])
    print(res)




