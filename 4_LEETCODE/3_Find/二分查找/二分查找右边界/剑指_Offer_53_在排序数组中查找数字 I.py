class Solution:
    def search(self, nums, target):
        '''
        二分查找左右边界
        '''

        def getL(nums, target):
            if not nums:
                return -1
            left, right = 0, len(nums)-1
            while left<right:
                mid = left + (right-left)//2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return left if nums[left] == target else -1

        def getR(nums, target):
            if not nums:
                return -1
            left, right = 0, len(nums)-1
            while left<right:
                mid = left+ (right-left+1)//2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid

            return right if nums[right]==target else -1

        L = getL(nums, target)
        R = getR(nums, target)
        return R-L+1 if L!=-1 else 0

if __name__ == '__main__':
    test = Solution()

    data = [1,2,3,4,4,4,4,4,5,6,7]
    target = 4

    res = test.search(data, target)

    print(res)

