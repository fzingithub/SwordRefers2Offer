# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:47:29 2019

@author: zhe
"""

class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num or len(num)<size or size==0:
            return []
        NumWindow = len(num) - size + 1
        res = []
        
        for i in range(NumWindow):
            res.append(max(num[i:i+size]))
            
        return res
    