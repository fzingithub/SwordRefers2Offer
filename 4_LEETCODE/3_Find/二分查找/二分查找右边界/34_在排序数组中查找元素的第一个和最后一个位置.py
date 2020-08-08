class Solution:
    def searchRange(self, nums, target):
        if not nums: return (-1, -1)
        left = self.GetLeftK(nums, target)
        right = self.GetRightK(nums, target)
        return (left, right)

    def GetLeftK(self, data, k):
        left, right  = 0, len(data) - 1
        while left < right:
            mid = left + (right - left) // 2
            if data[mid] < k:
                left = mid + 1
            else:
                right = mid
        return left if data[left] == k else -1

    def GetRightK(self, data, k):
        left, right  = 0, len(data) - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            if data[mid] > k:
                right = mid - 1
            else:
                left = mid
        return right if data[left] == k else -1

if __name__ == '__main__':
    test = Solution()
    data = [7,7,7,7,7,7,7,7,7]
    res = test.searchRange(data, 7)
    print(res)