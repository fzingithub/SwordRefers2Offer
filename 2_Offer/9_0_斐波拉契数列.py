# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 14:49:22 2018

@author: zhe

E-mail: 1194585271@qq.com
"""

#Solution1 递归 完全二叉树 时间 O(2^n)   空间 O(2^n)
class Solution1:
    def Fibonacci(self, n):
        # write code here
        if n<=0:
            return 0
        if n==1:
            return 1
        return self.Fibonacci(n-1)+self.Fibonacci(n-2)
    
#递归方法严重影响效率，会产生很多重复节点。


#Solution2 备忘录递归   时间 O(n)    空间 O(n)  #不考虑 python map 操作
class Solution2:
    def Fibonacci(self, n):
        # write code here
        if n<=0:
            return 0
        if n==1:
            return 1
        
        hashmap = {}
        if n in hashmap:
            return hashmap[n]
        else:
            value = self.Fibonacci(n-1)+self.Fibonacci(n-2)
            hashmap[n] = value
        return value


#Solution3 自底向上 时间 O(n) 空间 O(1)  实现真正的动态规划       
class Solution3:
    def Fibonacci(self, n):
        # write code here
        result = [0,1]
        if n<2:
            return result[n]        
        leftnum = 0
        rightnum = 1

        for i in range(1,n):
           leftnum , rightnum = rightnum ,leftnum+rightnum
        return rightnum
    

    


#O(logn)
#class Solution:
#    def Fibonacci(self, n):
#        # write code here
#        if n<=0:
#            return 0
#        if n==1:
#            return 1
#        import numpy as np
#        Mat = np.matrix([[1,1],[1,0]])
#        return int((Mat**n)[0][:,0])
# 
        
    
if __name__ == '__main__':
    Fi =Solution3()
    print (Fi.Fibonacci(30))      
    
    
    
    
