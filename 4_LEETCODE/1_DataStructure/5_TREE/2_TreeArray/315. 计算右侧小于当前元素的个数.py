class Solution:
    def countSmaller(self, nums):
        '''
        暴力： O(n^2) 超时
        '''

        if not nums:
            return []

        m = len(nums)

        res = []
        for i in range(m):
            tmp = 0
            for j in range(i + 1, m):
                if nums[i] > nums[j]:
                    tmp += 1
            res.append(tmp)

        return res

    def countSmaller1(self, nums):
        '''
        逆序插入   数组反过来插入一个有序数组（降序）中，插入的位置就是在原数组中位于它右侧的元素的个数。
        O(nlogn)
        '''
        import bisect
        sortns = []
        res = []
        for n in reversed(nums):
            idx = bisect.bisect_left(sortns, n)
            res.append(idx)
            sortns.insert(idx, n)
        return res[::-1]


if __name__ == '__main__':
    test = Solution()
    data = [5,2,6,1]
    res =test.countSmaller(data)

    print(res)