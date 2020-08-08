# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    pass

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n + 1

        while right - left > 1:
            mid = left + (right - left) // 2

            if guess(mid) == -1:
                right = mid
            else:
                left = mid

        return left if guess(left) == 0 else -1