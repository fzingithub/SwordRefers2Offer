# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 15:49:37 2018

@author: zhe

E-mail: 1194585271@qq.com
"""

class Solution:
    def rectCover(self, number):
        # write code here
        if number==0:
            return 0
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