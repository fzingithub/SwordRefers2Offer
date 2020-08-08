class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        if x == 2:
            return 1
        left = 1
        right = x - 1

        while left <= right:
            mid = left + (right - left) // 2
            if mid > x // mid:
                if mid - 1 < x // (mid - 1):
                    return mid - 1
                right = mid - 1
            elif mid < x // mid:
                left = mid + 1
            else:
                return mid

        return -1