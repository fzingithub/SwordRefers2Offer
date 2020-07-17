class Solution:
    # 暴力解法
    def trap1(self, height):
        res = 0
        length = len(height)
        for i in range(length):
            Lhigh = height[i]
            Rhigh = height[i]
            for j in range(length):
                if j < i:
                    Lhigh = max(Lhigh, height[j])
                elif j > i:
                    Rhigh = max(Rhigh, height[j])

            res += min(Lhigh, Rhigh) - height[i]

        return res

    # 动态编程
    def trap2(self, height):

        length = len(height)
        maxNum = 0
        Rhigh = []
        Lhigh = [0] * length
        for i in range(length):
            maxNum = max(maxNum, height[i])
            Rhigh.append(maxNum)

        maxNum = 0
        for i in range(length-1, -1, -1):
            maxNum = max(maxNum, height[i])
            Lhigh[i] = maxNum

        res = 0
        for i in range(length):
            res += min(Rhigh[i], Lhigh[i]) - height[i]

        return res

    # 单调栈
    def trap(self, height):
        if not height:
            return 0

        # 单调递增栈
        stack = []
        current = 0
        length = len(height)
        res = 0

        for current in range(length):
            while stack and height[stack[-1]] < height[current]:
                cur_index = stack.pop()
                if stack: # 形成水平低洼处
                    cur_bound = current - stack[-1] - 1 # 低洼宽度
                    cur_height = min(height[current], height[stack[-1]]) - height[cur_index] # 低洼高度
                    res += cur_bound * cur_height
            stack.append(current)

        return res

    # 双指针法 法二 动态编程推广
    def trap4(self, height):
        if not height:
            return 0

        maxL = 0
        maxR = 0
        pleft = 0
        pright = len(height) - 1
        res = 0

        while pleft<pright:
            if height[pleft]<height[pright]:
                if height[pleft] < maxL:
                    res += maxL - height[pleft]
                else:
                    maxL = height[pleft]
                pleft += 1
            else:
                if height[pright] < maxR:
                    res += maxR - height[pright]
                else:
                    maxR = height[pright]
                pright -= 1

        return res





if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]

    test = Solution()

    res = test.trap(height)

    print(res)