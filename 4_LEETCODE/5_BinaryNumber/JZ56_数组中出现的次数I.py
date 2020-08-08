class Solution:
    def singleNumbers(self, nums):

        res1, res2, s = 0, 0, 0

        for i in nums:
            s ^= i      # 找 res1 ^ res2

        mask = s & (-s)  # 找res1 res2 低位的不同位置

        for i in nums:  # 将数组分成两组
            if i & mask == mask:
                res1 ^= i
            else:
                res2 ^= i

        return res1, res2