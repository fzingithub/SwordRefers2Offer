# -*- coding: utf-8 -*-
'''
Created on 2019/6/30
Author: zhe
Email: 1194585271@qq.com
'''
import numpy as np
import time

class Sort():
    def shell_sort(self, data):
        length = len(data)

        gap = len(data)//2

        # 第一层循环是改变gap的值对列表进行分组
        while gap > 0:
            for i in range(gap, length):
                value = data[i]
                j = i - gap

                while j >= 0 and data[j] > value:
                    data[j+gap] = data[j]
                    j -= gap


                data[j+gap] = value
                # print(gap, data)

            gap = gap // 2
        return data

if __name__=='__main__':
    randomNum = np.random.randint(0, 1000000, size=100000)

    test = Sort()
    start = time.time()
    res = test.shell_sort(randomNum)
    end = time.time()

    print('time', end-start)
    print(res)