class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        left = 0
        right = len(arr)-k
        while left < right:
            mid = left + (right - left) // 2
            if abs(arr[mid]-x) > abs(arr[mid+k]-x):
                left = mid + 1
            else:
                right = mid

        return arr[left:left+k]