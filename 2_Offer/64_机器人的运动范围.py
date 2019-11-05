# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:15:14 2019

@author: zhe
"""

class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        matrix = matrix = [[False for i in range(cols)] for j in range(rows)]
        count = self.findGrid(threshold, rows, cols, matrix, 0, 0)
        return count
    
    def findGrid(self, threshold, rows, cols, matrix, i, j):
        count = 0
        if cols>j>=0 and rows>i>=0 and matrix[i][j]==False and self.judge(threshold, i, j):
            matrix[i][j] = True
            count = 1 + self.findGrid(threshold, rows, cols, matrix, i+1, j) \
                      + self.findGrid(threshold, rows, cols, matrix, i, j+1) \
                      + self.findGrid(threshold, rows, cols, matrix, i-1, j) \
                      + self.findGrid(threshold, rows, cols, matrix, i, j-1)
        return count
    
    def judge(self, threshold, i, j):
        if sum(map(int, str(i)+str(j))) <= threshold:
            return True
        return False
    
    
    
if __name__ == '__main__':
    test = Solution()
    res = test.movingCount(20, 44, 44)