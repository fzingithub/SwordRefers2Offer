# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 11:12:00 2018

@author: zhe

E-mail: 1194585271@qq.com
"""

class Solution:
    def __init__(self):
        self.dataS = [] #data stack
        self.minS = [] #min stack
    
    def push(self, node):
        self.dataS.append(node)
        if not self.minS:
            self.minS.append(node)
        else:
            if self.minS[-1] > node:
                self.minS.append(node)
            else:
                self.minS.append(self.minS[-1])

    def pop(self):
        # write code here
        self.minS.pop()
        return self.dataS.pop()
        
    def min(self):
        # write code here
        if self.minS:
            return self.minS[-1]
        
        
if __name__ == '__main__':
    a=Solution()
    for i in range(5):
        a.push(i)