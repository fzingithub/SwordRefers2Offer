class Solution:
    def findMin(self, nums):
        '''
        特例 原始查找左边界出错
        [7,7,7,7,7,7,7,7,7,8,9,1_最短回文串.py,7]
        '''
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return nums[left]

if __name__ == '__main__':
    test = Solution()
    data = [7,7,7,7,7,7,7,7,7,8,9,1,7]
    res = test.findMin(data)

    print(res)