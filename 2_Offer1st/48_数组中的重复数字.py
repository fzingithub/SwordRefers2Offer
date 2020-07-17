# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 12:40:10 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if not numbers:
            return False
        
        for index, value in enumerate(numbers):
            if index != value:
                if value == numbers[value]:
                    duplication[0] = value
                    return True
                else:
                    numbers[index], numbers[value] = numbers[value], numbers[index]
        return False
    
if __name__ == '__main__':
    test = Solution()
    a = [-1]
    res = test.duplicate([2,1,3,1,4], a)