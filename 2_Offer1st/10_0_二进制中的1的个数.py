# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 09:36:16 2018

@author: zhe

E-mail: 1194585271@qq.com
"""
##将正负整数转换为二进制补码
#def intToBin32(i):
#    return (bin(((1 << 64) - 1) & i)[2:]).zfill(64)

class Solution:
    def NumberOf1(self, n):
        # write code here
        return (bin(((1 << 32) - 1) & n)[2:]).zfill(32).count('1')
    
#res = Solution()
#print (res.NumberOf1(-999999))
        
#规律
#一个整数-1与自己做&与运算，会将二进制最右边的1变为0