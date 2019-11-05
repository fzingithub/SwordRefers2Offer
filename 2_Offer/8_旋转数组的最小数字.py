# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 11:50:15 2018

@author: zhe

E-mail: 1194585271@qq.com
"""

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        left = 0
        right = len(rotateArray)
        while left+1!=right:
            mid = (left+right)//2
            if rotateArray[mid] >= rotateArray[0]:
                left = mid
            else:
                right = mid
        return rotateArray[right]

#二分查找