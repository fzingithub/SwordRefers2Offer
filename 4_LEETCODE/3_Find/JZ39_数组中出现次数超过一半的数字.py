class Solution:
    def majorityElement(self, nums) -> int:
        '''
        数组中有一个数字出现的次数超过数组长度的一半，也就是说它出现的次数比其他所有数字出现次数的和还要多。
        我们可以考虑在遍历数组的时候保存两个值：一个是数组中的一个数字，一个是次数。

        '''
        num = nums[0]  # 从第一个元素开始
        counter = 1

        for i in nums[1:]:
            if i == num:
                counter += 1
            else:
                counter -= 1
                if counter == 0:
                    num = i
                    counter = 1

        return num