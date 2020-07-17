class Solution:
    # hash 时间O(n)， 空间O(n)
    def findRepeatNumber(self, nums):
        Map = {}
        for i in nums:
            if i in Map:
                return i
            else:
                Map[i] = 0

        return None

    def findRepeatNumber2(self, nums):
        AsL = [-1] * len(nums)

        for i in nums:
            if AsL[i] == 1:
                return i
            else:
                AsL[i] = 1

        return None

if __name__ == '__main__':
    test = Solution()

    res = test.findRepeatNumber2([2, 3, 1, 0, 2, 5, 3])

    print(res)
