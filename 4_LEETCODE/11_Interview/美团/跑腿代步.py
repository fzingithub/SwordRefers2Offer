class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        n = len(tinput)
        if k <= 0 or k > n:
            return list()
        start = 0
        end = n - 1
        mid = self.partition(tinput, start, end)
        while k - 1 != mid:
            if k - 1 > mid:
                start = mid + 1
                mid = self.partition(tinput, start, end)
            elif k - 1 < mid:
                end = mid - 1
                mid = self.partition(tinput, start, end)
        res = tinput[:mid + 1]
        return res

    def partition1(self, numbers, low, high):
        key, index = numbers[low]
        while low < high:
            while low < high and numbers[high][0] <= key:
                high -= 1
            numbers[low] = numbers[high]
            while low < high and numbers[low][0] >= key:
                low += 1
            numbers[high] = numbers[low]
        numbers[low] = (key, index)
        return low
    def partition(self, data, low, high):
        left = low
        right = high
        k, index = data[left]

        while left < right:
            while left < right and data[right][0] < k:     # not >=  otherwise IndexError: list index out of range
                right -= 1
            while left < right and data[left][0] >= k:
                left += 1
            if left < right:
                data[left], data[right] = data[right], data[left]
        data[low] = data[right]
        data[right] = (k,index)
        return right

n,m = map(int, input().split())

vals = [0] * (n+1)
weighs = [0] * (n+1)
rewards = []

for i in range(1, n+1):
    vals[i], weighs[i] = map(int, input().split())
    rewards.append((vals[i] + weighs[i]*2, i))

test = Solution()

nums_sorted = test.GetLeastNumbers_Solution(rewards, m)
print(nums_sorted)
res = sorted([i[1] for i in nums_sorted])

print(' '.join(map(str, res)))

'''
12 3
5 10
5 10
5 10
8 9
京东 4
7 9
6 10
7 9
5 10
5 10
5 10
5 10
'''