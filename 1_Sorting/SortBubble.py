# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 16:18:24 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

import numpy as np
import time

class Sort:
    def bubble_sort(self,data):
        for i in range(len(data)-1,0,-1):
            flag = False
            for j in range(i):
                if data[j]>data[j+1]:
                    data[j],data[j+1] = data[j+1],data[j]
                    flag = True
            if not flag:
                break
        return data #有返回的原地排序



if __name__=='__main__':
    randomNum = np.random.randint(0, 100000, size=10000)

    test = Sort()
    start = time.time()
    res = test.bubble_sort(randomNum)
    end = time.time()

    print('time', end-start)
    print(res)
        
    
    