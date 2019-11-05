# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 11:21:40 2019

@author: zhe

E-mail: 1194585271@qq.com
"""


#方法一： O(n^2)
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        
        if not array:
            return []
        
        lenA = len(array)
        for i in range(lenA-1, -1, -1):
            for j in range(i):
                if array[i]+array[j]==tsum:
                    return array[j],array[i]
        return []
    
    
#解法二， O(n)  充分利用有序的条件
class Solution1:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        
        left = 0;
        right = len(array)-1
        
        while left < right:
            if array[left]+array[right]==tsum:
                return array[left], array[right]
            elif array[left]+array[right]<tsum:
                left = left + 1
            else:
                right = right - 1
        return []
        
    
if __name__ == '__main__':
    test = Solution1()
    res = test.FindNumbersWithSum([1,2,4,7,8,11,13,14,15], 15)
    