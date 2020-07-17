# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 12:01:40 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

#解法一： 数组模拟整个过程  时间，O(mn)  空间，O(n)
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n<1 or m<1:
            return -1
        
        L = list(range(n))
        
        j=0
        while len(L) > 1:
            j = (j + m - 1) % len(L)
            L.remove(L[j])
            
        return L[0]
    
    
#解法二： 约瑟夫环的通用解法  时间，O(n)  空间，O(1])
class Solution1:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n<1 or m<1:
            return -1
        
        last = 0  #N=1时剩余小孩的新序号一定是0
        for i in range(2, n+1): #反推回去
            last = (last + m) % i
            
        return last


if __name__ == '__main__':
    test = Solution1()
    res = test.LastRemaining_Solution(98,8)