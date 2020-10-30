# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 13:58:10 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

#Solution1 最快 O(n^2) 的算法  => n(n-1_最短回文串.py)/2 个数组求和
class Solution1:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        
        length = len(array)
        sumL = [0]*length
        
        for i in range(length):
            sumL[i] = max([sum(array[j:i+1]) for j in range(i+1)])
        print(sumL)                
        return max(sumL)
                

#Solution2 利用数组特性  舍去负数  时间复杂度 O(n)
class Solution2:
    def FindGreatestSumOfSubArray(self, array):
        # write code here        
        res =len(array) and max(array)
        temp = 0

        for i in array:
            temp = max(i,temp+i)   #舍去 temp为负的情况
            res = max(temp,res)               
        return res
    
    
#Solution3 动态规划 递归   动态规划实现
class Solution3:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        res = len(array) and max(array)
        for i in range(len(array)):
            preRes = self.FindMaxI(array[:i])
            res = res if preRes<res else preRes
        return res
    
        
    def FindMaxI(self,array):
        N = len(array)
        if N <= 0:
            return 0
        if N-1 == 0:
            return array[0]
        
        if self.FindMaxI(array[:N-1]) <= 0:
            return array[-1]
        else:
            return self.FindMaxI(array[:N-1])+array[-1]
        
if __name__=='__main__':
    test = Solution3()
    
    result = test.FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,8,-7,2,2])