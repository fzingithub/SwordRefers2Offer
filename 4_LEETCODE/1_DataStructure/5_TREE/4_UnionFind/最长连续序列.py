class Solution:
    def longestConsecutive(self, nums):

        pre_dict = {}
        for i in nums:
            pre_dict[i] = 1

        res = 0
        for i in pre_dict:
            if i - 1 not in pre_dict:
                y = i + 1
                while y in pre_dict:
                    y += 1

                res = max(res, y - i)

        return res


test= Solution()

res = test.longestConsecutive([0])

print(res)
