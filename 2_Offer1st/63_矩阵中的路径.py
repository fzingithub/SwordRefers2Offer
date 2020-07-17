# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:17:51 2019

@author: zhe
"""

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        assistMatrix = [True]*rows*cols
        for i in range(rows):
            for j in range(cols):
                if self.findPath(matrix, rows, cols, path, i, j, assistMatrix):
                    return True
        return False
                
    def findPath(self, matrix, rows, cols, path, i, j, assistMatrix):
        '''
        find existing path with Backtracking method 
        '''
        if not path:
            return True
        index = i*cols+j
        
        if i<0 or i>=rows or j<0 or j>=cols or matrix[index]!=path[0] or assistMatrix[index]==False:
            return False
        
        assistMatrix[index] = False
        
        if (self.findPath(matrix, rows, cols, path[1:], i+1, j, assistMatrix) or
                self.findPath(matrix, rows, cols, path[1:], i-1, j, assistMatrix) or
                self.findPath(matrix, rows, cols, path[1:], i, j+1, assistMatrix) or
                self.findPath(matrix, rows, cols, path[1:], i, j-1, assistMatrix)):
            return True
        
        assistMatrix[index] = True
        
        return False
        
           