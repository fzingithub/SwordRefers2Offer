# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:33:47 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2 != 0:
            Sum = (num1 ^ num2) & 0xFFFFFFFF #对负数的处理
            Carry = ((num1 & num2) << 1) & 0xFFFFFFFF
            num1 = Sum
            num2 = Carry
        return num1 if num1<=0x7FFFFFFF else ~(num1^0xFFFFFFFF)



if __name__ == '__main__':
    test = Solution()
    res = test.Add(-15, 68)