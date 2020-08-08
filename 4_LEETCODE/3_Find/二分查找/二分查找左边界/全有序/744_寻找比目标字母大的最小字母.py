class Solution:
    def nextGreatestLetter(self, letters, target):
        left = 0
        right = len(letters)-1

        while left<right:
            mid = left + (right - left) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid

        return letters[left] if letters[left] > target else letters[0]