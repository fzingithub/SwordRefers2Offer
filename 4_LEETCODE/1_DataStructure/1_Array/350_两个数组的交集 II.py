class Solution:
    def intersection(self, nums1, nums2):
        '''
        返回两数组的交集， 可能有重复元素。
        暴力O(n^2)
        hash 优化 O(n)

        set 操作
        交集 intersection
        并集 union
        差集 difference
        '''
        length1 = len(nums1)
        length2 = len(nums2)

        if length2 < length1:   # 长度小的记为 num1
            nums1, nums2 = nums2, nums1

        mapNum1 = {}
        for i in nums1:
            if i in mapNum1:
                mapNum1[i] += 1
            else:
                mapNum1[i] = 1



        res = []
        for i in nums2:
            if i in mapNum1 and mapNum1[i]>0:
                res.append(i)
                mapNum1[i] -= 1

        return res


if __name__ == '__main__':
    test = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]

    res = test.intersection(nums1, nums2)


    print(res)