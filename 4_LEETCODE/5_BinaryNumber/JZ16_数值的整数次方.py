class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n < 0 and x:
            x = 1/x
            n = -n

        res = 1
        while n:
            if n&1:
                res *= x
            x = x*x
            n = n >> 1

        return res

if __name__ == '__main__':
    test = Solution()

    res = test.myPow(2,-2)

    print(res)
