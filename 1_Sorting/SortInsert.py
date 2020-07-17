# -*- coding: utf-8 -*-
'''
Created on 2019/6/27
Author: zhe
Email: 1194585271@qq.com
'''
import numpy as np
import time

class Sort():
    def insert_sort(self, data):


        for i in range(1, len(data)):
            value = data[i]  # 插入值
            j = i-1 # 记录插入位置  j+1 代表插入的位置

            while j >= 0 and data[j] > value:    # 不用 for 循环是因为 j 为 -1 的情况
                data[j+1] = data[j]
                j -= 1

            data[j+1] = value
            # print(data)
        return data


if __name__=='__main__':
    randomNum = np.random.randint(0, 100000, size=100)

    test = Sort()
    start = time.time()
    res = test.insert_sort(randomNum)
    end = time.time()

    print('time', end-start)
    print(res)
