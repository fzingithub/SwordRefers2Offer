# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 20:31:17 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        
        total = 5
        numbers.sort()
        numOfZero = numbers.count(0)
        
        numOfGap = 0
        for i in range(numOfZero, total-1):
            if numbers[i] == numbers[i+1]:
                return False
            numOfGap = numOfGap + numbers[i+1] - numbers[i]-1   #每两个判断间隙                                                       
        return True if numOfGap <= numOfZero else False

if __name__ == '__main__':
    test = Solution()
    res = test.IsContinuous([0, 1, 3, 5, 4])