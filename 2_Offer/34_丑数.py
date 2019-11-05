# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 12:14:17 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

#方法一，不考虑时间空间平衡问题  时间复杂度过大
class Solution1:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index<0:
            return 0
        
        number = 0
        uglyfound = 0
        
        while uglyfound<index:
            number = number + 1
            if self.isUgly(number):
                print (number)
                uglyfound = uglyfound + 1
        return number
        
        
    def isUgly(self,number):
        '''
        判断是否是丑数
        '''
        while number%5==0:
            number = number/5
        while number%3==0:
            number = number/3
        while number%2==0:
            number = number/2
        return True if number==1 else False
    
    
#以空间换取时间
class Solution2:
    def GetUglyNumber_Solution(self, index):
        # write code here
        '''
        利用丑数的特点：
        已有丑数，经过乘2，3或者5，
        且不再原数组中最小的便是下一个丑数。
        相比上述方法，不必非丑数上消耗时间。
        '''
        if index<=0:
            return 0
        uglyL = [1]   
        for i in range(1,index):
            maxUglyL = uglyL[-1]
            
            for i in uglyL:
                num2 = i * 2 
                if num2>maxUglyL:
                    break
                
            for i in uglyL:
                num3 = i * 3 
                if num3>maxUglyL:
                    break
            
            for i in uglyL:
                num5 = i * 5 
                if num5>maxUglyL:
                    break
            minUgly = min(num2,num3,num5)
            uglyL.append(minUgly)
            
        return uglyL[-1]
            
            
#精简解法
class Solution3:
    def GetUglyNumber_Solution(self, index):
        # write code here
        '''
        不必维护三个队列
        维护三个指针
        分别作用为 乘2,3或者5，最开始大于原数组最大的指针。
        '''
        if index<=0:
            return 0
        uglyL = [1]
        p2 = 0
        p3 = 0
        p5 = 0
        
        for i in range(1,index):
            uglyL.append(min(uglyL[p2]*2,uglyL[p3]*3,uglyL[p5]*5))
            if uglyL[-1]==uglyL[p2]*2:
                p2 = p2 + 1
            if uglyL[-1]==uglyL[p3]*3:
                p3 = p3 + 1
            if uglyL[-1]==uglyL[p5]*5:
                p5 = p5 + 1              
        return uglyL[-1]            
            
         
        
        
        
    
    
if __name__ == '__main__':
    import time
    start = time.time()
    
    
    test = Solution3()
    res = test.GetUglyNumber_Solution(1000)
    
    
    end = time.time()
    print ('Running time: %s seconds' % (end-start))
    
    
        