class Solution:
    # 冒泡 O(n^2)
    def reversePair(self, nums):
        res = 0
        length = len(nums)
        for i in range(length):
            flag = 0
            for j in range(length-1,i,-1):
                if nums[j]<nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    res += 1
                    flag = 1

            if flag==0:
                break

        return res

    # 归并 O(nlogn)
    def __init__(self):
        self.PairNum = 0

    def reversePair1(self, nums):
        _ = self.merge_sort(nums)

        return self.PairNum

    def merge_sort(self, nums):
        length = len(nums)
        if length < 2:
            return nums

        mid = length//2

        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return self.merge(left, right)

    def merge(self, data1, data2):
        nums = []
        length2 = len(data2)

        while data1 and data2:
            if data2[0]<data1[0]:
                self.PairNum += len(data1)
                nums.append(data2.pop(0))
            else:
                nums.append(data1.pop(0))


        nums.extend(data1) if data1 else nums.extend(data2)
        return nums







if __name__ == '__main__':
    test = Solution()

    nums = [7,5,6,4]
    res = test.reversePair1(nums)

    print(res)