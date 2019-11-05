# -*- coding: utf-8 -*-
import numpy as np
import time


class Sort:
    def quick_sort(self, data, left, right):
        if left < right:
            k_idx = self.partation1(data, left, right)
            self.quick_sort(data, left, k_idx - 1)
            self.quick_sort(data, k_idx + 1, right)
        return data

    # 左右指针
    def partation(self, data, low, high):
        left = low
        right = high
        k = data[left]

        while left < right:
            while left < right and data[right] > k:     # not >=  otherwise IndexError: list index out of range
                right -= 1
            while left < right and data[left] <= k:
                left += 1
            if left < right:
                data[left], data[right] = data[right], data[left]
        data[low] = data[right]
        data[right] = k
        return right

    # 填坑法
    def partation1(self, data, low, high):
        left = low
        right = high
        k = data[left]
        while left < right:
            while left < right and data[right] >= k:
                right -= 1
            if  left < right:
                data[left] = data[right]
            while left < right and data[left] <= k:
                left += 1
            if left < right:
                data[right] = data[left]

        data[left] = k
        return left



if __name__ == '__main__':
    randomNum = np.random.randint(0, 100000, size=10000)

    test = Sort()
    start = time.time()
    res = test.quick_sort(randomNum, 0, len(randomNum)-1)
    end = time.time()

    print('time', end-start)
    print(res)