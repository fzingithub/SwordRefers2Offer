# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 09:01:45 2018

@author: zhe

E-mail: 1194585271@qq.com
"""

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if matrix == None:
            return None
        
        row = len(matrix)
        col = len(matrix[0])
        
        if row <= 0 or col <= 0 :
            return 
        
        result = []
        start = 0
        while start*2 < row and start*2 < col:
            self.PrintMatrixInCicle(matrix,start,result,row,col)
            start += 1
            
        return result
            
    def PrintMatrixInCicle(self,matrix,start,result,row,col):
        endX = col-1-start
        endY = row-1-start
        #从左到右
        j = start
        while j <= endX:
            result.append(matrix[start][j])
            j += 1
            
        #从上到下
        i = start + 1
        while i <= endY:
            result.append(matrix[i][endX])
            i += 1
            
        if endX == start or endY == start:
            return
        #从右到左
        j = endX -1
        while j >= start:
            result.append(matrix[endY][j])
            j -= 1
            
        #从下到上
        i = endY - 1
        while i >= start + 1:
            result.append(matrix[i][start])
            i -= 1
        
a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        
test = Solution()

print (test.printMatrix(a))
        