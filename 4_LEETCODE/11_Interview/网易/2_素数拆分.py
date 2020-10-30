class Solution:
    def split(self, nums):
        res = 0

        def splitNum(num):
            return num//2

        for num in nums:
            res += splitNum(num)

        return res

if __name__ == '__main__':
    test = Solution()
    nums = [3,5,7]

    res = test.split(nums)

    print(res)
