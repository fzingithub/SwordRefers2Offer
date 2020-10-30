# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1_最短回文串.py 12:00:44 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

#方法一， 利用python str + 以及切片操作
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        return s[n:]+s[:n]



if __name__ == '__main__':
    test = Solution()
    res = test.LeftRotateString('186479523', 3)
                  