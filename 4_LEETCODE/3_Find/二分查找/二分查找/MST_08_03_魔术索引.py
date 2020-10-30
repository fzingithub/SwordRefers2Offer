class Solution:
    def findMagicIndex(self, nums:list)->int:
        '''
        [0,3,2,4,1_最短回文串.py]

        方法一：暴力。
        '''
        for index, element in enumerate(nums):
            if index == element:
                return index

        return -1


    def findMagicIndex(self, nums:list)->int:
        '''
        [0,3,2,4,1_最短回文串.py]

        方法一：二分剪枝 + 递归。
        '''
        left, right = 0, len(nums)-1
        return self.search(nums, left, right)

    def search(self, nums, left, right):
        if left>right:
            return -1

        mid = left + (right-left)//2
        if mid==nums[mid]:
            res = self.search(nums, left, mid-1)
            if res!=-1:
                return res
            else:
                return mid
        else:
            res = self.search(nums, left, mid-1)
            if res!=-1:
                return res
            res = self.search(nums, mid+1, right)
            if res!=-1:
                return res
        return -1

if __name__ == '__main__':
    test = Solution()

    data = [0,2,2,2,2,2]
    res = test.findMagicIndex(data)

    print(res)