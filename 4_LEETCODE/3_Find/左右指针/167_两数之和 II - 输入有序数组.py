class Solution:
    def twoSum(self, numbers, target):
        n = len(numbers)

        if n < 2:
            return (-1, -1)

        left, right = 0, n - 1

        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                break

        return (left + 1, right + 1)