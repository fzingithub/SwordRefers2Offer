# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:52:37 2019

@author: zhe

E-mail: 1194585271@qq.com
"""
# python 但实际不符合要求
class Solution:
    def Sum_Solution(self, n):
        # write code here
        return sum(range(n+1))


#要注意python中逻辑运算符的用法，a  and  b，a为False，返回a，a为True，就返回b
class Solution1:
    def Sum_Solution(self, n):
        # write code here
        return n and n+self.Sum_Solution(n-1)
        

if __name__ == '__main__':
    test = Solution1()
    res = test.Sum_Solution(5)

    print(res)