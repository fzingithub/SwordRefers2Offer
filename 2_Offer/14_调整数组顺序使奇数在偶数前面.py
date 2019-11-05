# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 15:17:17 2018

@author: zhe

E-mail: 1194585271@qq.com
"""

class Solution:
    def reOrderArray(self, array):
        # write code here
        pbegin = 0
        pend = len(array)- 1
        
        while pbegin <= pend:
            while pbegin <= pend and self.reOrderOddEven(pbegin,array): #find Odd return Ture
                pbegin = pbegin + 1

            while pbegin <= pend and not self.reOrderOddEven(pend,array):
                pend = pend - 1
            
            if pbegin < pend:
                array[pbegin],array[pend] = array[pend],array[pbegin]
            
#        print (array)
#        print (pbegin,pend)
                
        L = sorted(array[:pend+1])
        L.extend(sorted(array[pend+1:]))
                
        return L
        
        
    def reOrderOddEven(self,pbegin,array):
        if array[pbegin] % 2 == 0:
            return False
        else:
            return True
        
        
testL = [1,2,3,4,5,6,7]
test = Solution()

print (test.reOrderArray(testL))