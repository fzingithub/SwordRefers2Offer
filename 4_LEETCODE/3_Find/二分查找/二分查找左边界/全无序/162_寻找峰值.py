class Solution(object):
    def findPeakElement(self, nums):
        '''
        不能有连续的相同元素
        '''

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == '__main__':
    test = Solution()

    data = [2,6,5,4,10,4,6,9,1,4,7,3,6,5,1]

    res = test.findPeakElement(data)

    print(res)