# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 18:07:39 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        return self.isSymmetrical2(pRoot, pRoot)
    
    
    def isSymmetrical2(self, pLRoot, pRRoot):
        if pLRoot and pRRoot and pLRoot.val==pRRoot.val:
            return self.isSymmetrical2(pLRoot.left,pRRoot.right) and self.isSymmetrical2(pLRoot.right,pRRoot.left)
        elif not pLRoot and not pRRoot:
            return True
        else:
            return False
            

        