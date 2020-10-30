class Solutoin:
    def searchInsert(self, nums, target):
        '''
        方法一：暴力
        [1_最短回文串.py,3,5,7], 6
        '''

        i = 0
        while i<len(nums):
            if target[i]>=target:
                return i

        return i

    def searchInsert(self, nums, target):
        '''
        方法一：二分查找左边界 左移近 右不变 mid 向下取整    right=mid
        [1_最短回文串.py,3,5,7], 6
        '''

        '''
                方法一：二分
                [1_最短回文串.py,3,5,7], 6
                '''

        def biSearch(nums, target, left, right):
            if left == right:
                return left

            mid = (left + right) // 2
            if nums[mid] < target:
                res = biSearch(nums, target, mid + 1, right)
            else:
                res = biSearch(nums, target, left, mid)

            return res

        n = len(nums)
        if not n:
            return 0

        res = biSearch(nums, target, 0, n - 1)
        res = res + 1 if res == n - 1 and target > nums[-1] else res

        return res

    def searchInsert(self, nums, target):
        '''
        方法一：二分查找左边界 左移近 右不变 mid 向下取整    right=mid
        [1_最短回文串.py,3,5,7], 6
        '''

        '''
                方法一：二分
                [1_最短回文串.py,3,5,7], 6
                '''

        def biSearch(nums, target, left, right):

            while left<right:
                mid = left + (right-left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return left if nums[left] >= target else right+1

        n = len(nums)
        if not n:
            return 0

        res = biSearch(nums, target, 0, n - 1)

        return res

if __name__ == '__main__':
    test = Solutoin()
    data = [3,4,5,7,8,9,9,9]
    target = 7

    res = test.searchInsert(data, target)

    print(res)

