# -*- coding: utf-8 -*-
import numpy as np
import time


class Sort:
    def quick_sort(self, data, left, right):
        if left < right:
            k_idx = self.partation(data, left, right)
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
    # res = test.quick_sort(randomNum, 0, len(randomNum)-1)

    data = [41,23,87,55,50,53,18,9,39,63,35,33,54,25,26,49,74,61,32,81,97,99,38,96,22,95,35,57,80,80,16,22,17,13,89,11,75,98,57,81,69,8,10,85,13,49,66,94,80,25,13,85,55,12,87,50,28,96,80,43,10,24,88,52,16,92,61,28,26,78,28,28,16,1,56,31,47,85,27,30,85,2,30,51,84,50,3,14,97,9,91,90,63,90,92,89,76,76,67,55]
    data = [8, 8, 12,5,7,2,9,8]
    res = test.quick_sort(data, 0, len(data)-1)
    end = time.time()

    print('time', end-start)
    print(res)