# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 13:22:52 2018

@author: zhe

E-mail: 1194585271@qq.com
"""
array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rows = len(array)-1
        cols = len(array[0])-1
        
        r = 0
        c = cols
        while r<=rows and c>=0:
#            print (r,c)           #搜索路径
            if target < array[r][c]:
                c -= 1
            elif target > array[r][c]:
                r += 1
            else:
                return True               
        return False
    
if __name__== '__main__':    
    sol = Solution()
    print (sol.Find(10,array))