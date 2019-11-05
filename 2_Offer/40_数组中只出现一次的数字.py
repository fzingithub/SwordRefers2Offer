# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 09:44:42 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

#解法一： 时间 O(n)， 空间 (1)      用异或的交换律
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if (not array) or len(array)<2:
            return
        
        XORF = 0
        for e in array:   #for finding first bit 1
            XORF = XORF ^ e
        
        indexIs1 = self.FindFirstBitIs1(XORF)
        
        XORA=XORB=0
        for e in array:
            if self.IsBit1(e,indexIs1):
                XORA = XORA ^ e
            else:
                XORB = XORB ^ e
                
        return XORA, XORB
    
    def FindFirstBitIs1(self, numBit):   #为了将数组划分成两个子数组
        if numBit == 0:
            return None
        indexBit = 0
        while (indexBit & 1)==0:
            numBit = numBit >> 1
            indexBit = indexBit + 1
        return indexBit
    
    def IsBit1(self, num, numbit):
        num = num >> numbit
        return (num & 1)
        
        
         
#解法二： hashMap法  时间 O(n), 空间 O(n)
class Solution1:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        hashMap = {}
        for i in array:
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1
        res = []
        for k in hashMap.keys():
            if hashMap[k] == 1:
                res.append(k)
        return res
        
        
        
        
        