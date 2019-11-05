# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 20:11:41 2018

@author: zhe

E-mail: 1194585271@qq.com
"""
#事实上是一个大数问题    但是python 整数不会溢出 实现了字符串整型运算符
class Solution:
    def print1toN(self, n):
        if n<=0 :
            print ("Invalid Input!")
            return None
        for i in range(10**n):
            print (i,end=' ')
        return None
            
test = Solution()

test.print1toN(4)