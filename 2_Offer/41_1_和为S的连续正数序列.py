# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 11:11:28 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

#方法 借鉴两个指针 
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        
        if tsum<3:
            return []
        
        small = 1
        big = 2
        middle = (tsum+1)//2
        sumL = small + big
        res = []
        
        while small < middle: 
            if sumL == tsum:
                res.append(list(range(small,big+1)))
                
            while sumL > tsum and small < middle:
                sumL = sumL - small
                small = small + 1
                if sumL == tsum:
                    res.append(list(range(small,big+1)))
            big = big + 1
            sumL = sumL + big

        return res
    
if __name__ == '__main__':
    test = Solution()
    res = test.FindContinuousSequence(9)