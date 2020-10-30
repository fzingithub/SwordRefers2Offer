class Solution:
    def find_prime(self, nums):
        res = []

        def isprime(n):
            import math
            if n < 2: return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True

        for num in nums:
            if isprime(num):
                res.append(num)

        return res


if __name__ == '__main__':
    test = Solution()
    res = test.find_prime([2,3,5,8,10])
    print(res)
