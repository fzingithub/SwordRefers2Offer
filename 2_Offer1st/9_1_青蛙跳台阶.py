# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 15:12:19 2018

@author: zhe

E-mail: 1194585271@qq.com
"""

class Solution:
    def jumpFloor(self, number):
        # write code here
        if number==1:
            return 1
        if number==2:
            return 2
        
        leftnumber = 1
        rightnumber = 2
        i=3
        while i<=number:
            leftnumber,rightnumber = rightnumber,leftnumber+rightnumber
            i = i+1
        return rightnumber


##青蛙变态跳台阶
#class Solution:
#    def jumpFloor(self, number):
#        # write code here
#        return 2**(n-1_最短回文串.py)