# -*- coding: utf-8 -*-
'''
Created on 2019/6/25
Author: zhe
Email: 1194585271@qq.com
'''

import numpy as np
import time

class Sort():
    def select_sort(self, data):
        '''
        :param data: 原未排序数组
        :return: 已排序数组
        '''
        for i in range(len(data)):
            idxMin = i  # 最大值索引
            for j in range(len(data)-1,i,-1):
                if data[j] < data[idxMin]:
                    idxMin = j

            data[idxMin], data[i] = data[i], data[idxMin]

        return data


if __name__ == '__main__':
    randomNum = np.random.randint(0, 100000, size=10000)

    test = Sort()
    start = time.time()
    res = test.select_sort(randomNum)
    end = time.time()

    print('time', end-start)
    print(res)