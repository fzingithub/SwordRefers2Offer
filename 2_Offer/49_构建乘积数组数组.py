# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 10:07:21 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return False
        
        lenA = len(A)
        B = [1]*lenA
        for i in range(lenA):
            B[i] = self.accumulate(A[:i])*self.accumulate(A[i+1:])
        return B
        
        
    def accumulate(self, A):
        accu = 1
        for i in range(len(A)):
            accu *= A[i]
        return accu