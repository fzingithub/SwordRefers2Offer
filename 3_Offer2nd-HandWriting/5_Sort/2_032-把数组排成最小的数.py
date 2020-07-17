class Solution:
    '''
    [1,5,8,3,7,10]
    greater a>b:'ab'>'ba'
    '''
    # 冒泡 O(n^2)
    def minNumber(self, nums):
        length = len(nums)
        nums = list(map(str, nums))
        for i in range(length):
            flag = 0
            for j in range(length-1, i,-1):
                if self.cmp(nums[j-1], nums[j]):
                    nums[j-1], nums[j] = nums[j], nums[j-1]
                    flag = 1

            if flag==0:
                break

        res = ''.join(nums)
        return res

    def minNumber1(self, nums):
        length = len(nums)
        nums = list(map(str, nums))
        self.quick_sort(nums, 0, length-1)
        return ''.join(nums)


    def quick_sort(self, data, left, right):
        if left < right:
            k_idx = self.partition(data, left, right)
            self.quick_sort(data, left, k_idx - 1)
            self.quick_sort(data, k_idx + 1, right)

    # 左右指针
    def partition(self, data, low, high):
        left = low
        right = high
        k = data[left]

        while left < right:
            while left < right and self.cmp(data[right], k):     # not >=  otherwise IndexError: list index out of range
                right -= 1
            while left < right and not self.cmp(data[left], k):
                left += 1
            if left < right:
                data[left], data[right] = data[right], data[left]
        data[low], data[right] = data[right], data[low]
        return right


    def cmp(self, a, b):
        '''
        :param a:  str
        :param b:  str
        :return:  'ab' > 'ba'
        '''

        return a+b > b+a


if __name__ == '__main__':
    test = Solution()

    res = test.minNumber1(
        [41,23,87,55,50,53,18,9,39,63,35,33,54,25,26,49,74,61,32,81,97,99,38,96,22,95,35,57,80,80,16,22,17,13,89,11,75,98,57,81,69,8,10,85,13,49,66,94,80,25,13,85,55,12,87,50,28,96,80,43,10,24,88,52,16,92,61,28,26,78,28,28,16,1,56,31,47,85,27,30,85,2,30,51,84,50,3,14,97,9,91,90,63,90,92,89,76,76,67,55]
    )

    print(res)