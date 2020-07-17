# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 11:16:08 2018

@author: zhe

E-mail: 1194585271@qq.com
"""

#不允许调用库函数
#class Solution:
#    def Power(self, base, exponent):
#        # write code here
#        return base**exponent

class Solution:
    InputInvalid = False
    def Power(self, base, exponent):
        # write code here
        self.InputInvalid = False
        if self.equal(base,0.0) and exponent<0:
            self.InputInvalid = True
#            print ('Input Invalid!')
            return 0.0
        
        absexponent = abs(exponent)
        result = self.FastPowerWithUnsignedExponent(float(base),float(absexponent))
        if exponent<0:
            return 1.0/result
        
        return result
    
    def PowerWithUnsignedExponent(self,base,absexponent):
        result = 1.0
        
        i=1
        while i<=absexponent:
            result = result*base
            i = i+1
        return result\
    
    def FastPowerWithUnsignedExponent(self,base,absexponent):
        if absexponent == 0:
            return 1
        if absexponent == 1:
            return base
        
        result = self.FastPowerWithUnsignedExponent(base,int(absexponent)>>1)
        result = result * result
        
        if (int(absexponent) & 0x1) == 1:
            result = base *result
        
        return result
        
        
    
    def equal(self,fnum1,fnum2):
        if 0.00000001>(fnum1-fnum2)>-0.00000001 :
            return True
        else:
            return False
        
        
test = Solution()
print (test.Power(1.2,6))
        
