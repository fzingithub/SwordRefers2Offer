class Solution:
    def isStraight(self, nums: 'List[int]') -> bool:
        '''
        设置零个数变量
        排序后，插值，零因子减为负数的时候 返回False ，否则返回True
        '''
        nums.sort()
        numZero = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                numZero += 1
            else:
                break

        for j in range(i + 1, len(nums)):

            num = nums[j - 1]
            while nums[j] != num + 1:
                numZero -= 1
                num += 1
                if numZero < 0:
                    return False

        return True



