class Solution:
    def maxSildingWindow(self, nums, k):
        length = len(nums)
        if not nums or k<0 or length<k:
            return []


        pleft = 0
        pright = 0
        Queue = [] #维护一张双端的非减单调队列 存索引 [8, 4, -2， -2， -7]
        res = []
        while pright<length:
            if pright-pleft+1 < k: # 未形成窗口
                while Queue and nums[pright] > nums[Queue[-1]]:
                    Queue.pop()
                Queue.append(pright)
                pright += 1
            else: # 形成窗口
                while Queue and nums[pright] > nums[Queue[-1]]:
                    Queue.pop()
                Queue.append(pright)

                while Queue[0]<pleft: # 划过最大值
                    Queue.pop(0)

                res.append(nums[Queue[0]])
                pright += 1
                pleft += 1

        return res


if __name__ == '__main__':
    test = Solution()

    data = [1,3,-1,-3,5,3,6,7]
    res = test.maxSildingWindow(data, 3)
    print(res)
